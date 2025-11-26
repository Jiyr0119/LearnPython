import asyncio
import base64
import json
import tempfile
import os
from pyppeteer import launch


async def xml_to_png_base64(xml: str):
    """
    使用 Draw.io 的嵌入 API 将 XML 转换为 PNG base64
    
    Draw.io 嵌入模式使用 postMessage 协议进行通信
    文档: https://www.drawio.com/doc/faq/embed-mode
    """
    
    # 创建一个 HTML 页面来嵌入 Draw.io
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body { margin: 0; padding: 0; }
            #drawio-frame { width: 100vw; height: 100vh; border: none; }
        </style>
    </head>
    <body>
        <iframe id="drawio-frame" src="https://embed.diagrams.net/?embed=1&ui=min&spin=1&proto=json"></iframe>
        <script>
            let drawioFrame = document.getElementById('drawio-frame');
            let exportPromiseResolve = null;
            let exportPromiseReject = null;
            
            // 监听来自 Draw.io 的消息
            window.addEventListener('message', function(evt) {
                if (evt.data.length > 0) {
                    try {
                        let msg = JSON.parse(evt.data);
                        console.log('Received message:', msg.event);
                        
                        // Draw.io 初始化完成
                        if (msg.event === 'init') {
                            console.log('Draw.io initialized');
                            drawioFrame.contentWindow.postMessage(JSON.stringify({
                                action: 'load',
                                autosave: 0
                            }), '*');
                        }
                        
                        // 加载完成,可以设置 XML
                        if (msg.event === 'load') {
                            console.log('Draw.io loaded, setting XML...');
                            // 标记为已准备好
                            window.drawioReady = true;
                        }
                        
                        // 导出完成
                        if (msg.event === 'export') {
                            console.log('Export completed');
                            if (exportPromiseResolve) {
                                exportPromiseResolve(msg.data);
                            }
                        }
                        
                        // 错误处理
                        if (msg.event === 'error') {
                            console.error('Draw.io error:', msg);
                            if (exportPromiseReject) {
                                exportPromiseReject(new Error(msg.message || 'Unknown error'));
                            }
                        }
                    } catch (e) {
                        console.log('Non-JSON message:', evt.data);
                    }
                }
            });
            
            // 提供给外部调用的函数
            window.loadXmlAndExport = function(xmlData) {
                return new Promise((resolve, reject) => {
                    exportPromiseResolve = resolve;
                    exportPromiseReject = reject;
                    
                    // 等待 Draw.io 准备好
                    let checkReady = setInterval(() => {
                        if (window.drawioReady) {
                            clearInterval(checkReady);
                            
                            // 加载 XML
                            console.log('Loading XML data...');
                            drawioFrame.contentWindow.postMessage(JSON.stringify({
                                action: 'load',
                                xml: xmlData,
                                autosave: 0
                            }), '*');
                            
                            // 等待一下让图表渲染
                            setTimeout(() => {
                                console.log('Requesting export...');
                                drawioFrame.contentWindow.postMessage(JSON.stringify({
                                    action: 'export',
                                    format: 'png',
                                    scale: 1,
                                    border: 10
                                }), '*');
                            }, 2000);
                        }
                    }, 100);
                    
                    // 30秒超时
                    setTimeout(() => {
                        reject(new Error('Export timeout'));
                    }, 30000);
                });
            };
        </script>
    </body>
    </html>
    """
    
    # 保存 HTML 到临时文件
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
        f.write(html_content)
        html_path = f.name
    
    try:
        browser = await launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu"
            ]
        )
        page = await browser.newPage()
        
        # 启用控制台日志
        page.on('console', lambda msg: print(f'Browser console: {msg.text}'))

        print("Loading Draw.io embed page...")
        await page.goto(f'file://{html_path}', waitUntil='networkidle2', timeout=60000)
        
        print("Waiting for Draw.io to initialize...")
        # 等待 loadXmlAndExport 函数可用
        await page.waitForFunction("typeof window.loadXmlAndExport === 'function'", timeout=60000)
        
        print("Draw.io ready, loading XML and exporting...")
        # 调用函数加载 XML 并导出
        xml_escaped = json.dumps(xml)
        png_base64 = await page.evaluate(f"() => window.loadXmlAndExport({xml_escaped})")
        
        await browser.close()
        
        # 如果返回的是纯 base64,添加 data URI 前缀
        if not png_base64.startswith('data:'):
            png_base64 = f"data:image/png;base64,{png_base64}"
        
        print("Export successful!")
        return png_base64
        
    finally:
        # 清理临时文件
        if os.path.exists(html_path):
            os.remove(html_path)


# ---------------------------
# 使用示例
# ---------------------------
if __name__ == "__main__":
    xml = """
    <mxfile>
      <diagram id="example" name="Page-1">
        <mxGraphModel>
          <root>
            <mxCell id="0"/>
            <mxCell id="1" parent="0"/>
            <mxCell id="2" value="Hello Drawio" style="text" vertex="1" parent="1">
              <mxGeometry x="20" y="20" width="120" height="40" as="geometry"/>
            </mxCell>
          </root>
        </mxGraphModel>
      </diagram>
    </mxfile>
    """

    base64_png = asyncio.run(xml_to_png_base64(xml))
    print(f"\nGenerated PNG base64 (first 100 chars):")
    print(base64_png[:100])
    print(f"\nTotal length: {len(base64_png)} characters")
    
    # 保存为 PNG 文件
    output_file = "drawio_output.png"
    
    # 从 data URI 中提取 base64 数据
    if base64_png.startswith('data:image/png;base64,'):
        base64_data = base64_png.replace('data:image/png;base64,', '')
    else:
        base64_data = base64_png
    
    # 解码并保存
    png_bytes = base64.b64decode(base64_data)
    with open(output_file, 'wb') as f:
        f.write(png_bytes)
    
    print(f"\n✅ PNG 文件已保存到: {os.path.abspath(output_file)}")
    print(f"文件大小: {len(png_bytes)} bytes")



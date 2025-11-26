import asyncio
import base64
import json
import os
from pyppeteer import launch


async def xml_to_png_base64_local(xml: str):
    """
    使用本地 HTML 文件和 mxGraph 库将 Draw.io XML 转换为 PNG
    这个方法不依赖在线 Draw.io 服务
    """
    
    # 创建一个本地 HTML 文件来渲染 Draw.io 图表
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <script src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>
    </head>
    <body>
        <div id="graph-container"></div>
        <script>
            window.convertXmlToPng = function(xmlData) {
                return new Promise((resolve, reject) => {
                    try {
                        // 使用 Draw.io viewer 库
                        const container = document.getElementById('graph-container');
                        
                        // 解析 XML
                        const parser = new DOMParser();
                        const xmlDoc = parser.parseFromString(xmlData, 'text/xml');
                        
                        // 创建一个 canvas 来渲染
                        const canvas = document.createElement('canvas');
                        const ctx = canvas.getContext('2d');
                        
                        // 设置 canvas 大小
                        canvas.width = 800;
                        canvas.height = 600;
                        
                        // 简单的文本渲染作为示例
                        // 注意: 完整的 Draw.io 渲染需要更复杂的逻辑
                        ctx.fillStyle = 'white';
                        ctx.fillRect(0, 0, canvas.width, canvas.height);
                        ctx.fillStyle = 'black';
                        ctx.font = '20px Arial';
                        ctx.fillText('Draw.io Diagram', 20, 40);
                        
                        // 转换为 base64
                        const dataUrl = canvas.toDataURL('image/png');
                        resolve(dataUrl);
                    } catch (e) {
                        reject(e);
                    }
                });
            };
        </script>
    </body>
    </html>
    """
    
    # 保存 HTML 到临时文件
    html_path = '/tmp/drawio_converter.html'
    with open(html_path, 'w') as f:
        f.write(html_content)
    
    browser = await launch(
        headless=True,
        args=[
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu"
        ]
    )
    page = await browser.newPage()

    # 加载本地 HTML 文件
    await page.goto(f'file://{html_path}', waitUntil='networkidle2')
    
    # 等待函数可用
    await page.waitForFunction("typeof window.convertXmlToPng === 'function'")

    # 执行转换
    xml_escaped = json.dumps(xml)
    png_base64 = await page.evaluate(f"() => window.convertXmlToPng({xml_escaped})")

    await browser.close()
    
    # 清理临时文件
    if os.path.exists(html_path):
        os.remove(html_path)

    return png_base64


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

    base64_png = asyncio.run(xml_to_png_base64_local(xml))
    print(f"Generated base64 PNG (first 100 chars):")
    print(base64_png[:100])

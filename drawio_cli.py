import subprocess
import base64
import tempfile
import os


def xml_to_png_base64_cli(xml: str) -> str:
    """
    使用 Draw.io CLI 将 XML 转换为 PNG base64
    
    前提条件:
    1. 安装 Draw.io 桌面版: brew install --cask drawio
    2. 或从 https://github.com/jgraph/drawio-desktop/releases 下载
    """
    
    # 创建临时文件
    with tempfile.NamedTemporaryFile(mode='w', suffix='.drawio', delete=False) as xml_file:
        xml_file.write(xml)
        xml_path = xml_file.name
    
    png_path = xml_path.replace('.drawio', '.png')
    
    try:
        # 使用 Draw.io CLI 导出为 PNG
        # macOS 上的 Draw.io 路径
        drawio_path = "/Applications/draw.io.app/Contents/MacOS/draw.io"
        
        # 检查 Draw.io 是否安装
        if not os.path.exists(drawio_path):
            raise FileNotFoundError(
                f"Draw.io not found at {drawio_path}\n"
                "Please install it: brew install --cask drawio"
            )
        
        # 执行导出命令
        subprocess.run([
            drawio_path,
            "--export",
            "--format", "png",
            "--output", png_path,
            xml_path
        ], check=True, capture_output=True)
        
        # 读取生成的 PNG 并转换为 base64
        with open(png_path, 'rb') as png_file:
            png_data = png_file.read()
            png_base64 = base64.b64encode(png_data).decode('utf-8')
            return f"data:image/png;base64,{png_base64}"
    
    finally:
        # 清理临时文件
        if os.path.exists(xml_path):
            os.remove(xml_path)
        if os.path.exists(png_path):
            os.remove(png_path)


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

    try:
        base64_png = xml_to_png_base64_cli(xml)
        print(f"Success! Generated base64 PNG (first 100 chars):")
        print(base64_png[:100])
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Draw.io export failed: {e}")
        print(f"stderr: {e.stderr.decode()}")

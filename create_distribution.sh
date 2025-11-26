#!/bin/bash

# Python 项目打包脚本
# 类似前端项目删除 node_modules 后打包

PROJECT_NAME="learnPython"
OUTPUT_FILE="${PROJECT_NAME}_distribution.zip"

echo "📦 开始打包 Python 项目..."
echo "排除: venv/, __pycache__/, *.pyc 等文件"
echo ""

# 使用 zip 命令,排除不需要的文件和目录
zip -r "$OUTPUT_FILE" . \
    -x "venv/*" \
    -x "__pycache__/*" \
    -x "*/__pycache__/*" \
    -x "*.pyc" \
    -x "*.pyo" \
    -x "*.pyd" \
    -x ".Python" \
    -x "*.so" \
    -x "*.egg-info/*" \
    -x ".pytest_cache/*" \
    -x ".coverage" \
    -x "htmlcov/*" \
    -x ".git/*" \
    -x ".DS_Store" \
    -x "*.swp" \
    -x ".idea/*" \
    -x ".vscode/*" \
    -x "*.log" \
    -x "drawio_output.png"

echo ""
echo "✅ 打包完成!"
echo "📁 输出文件: $OUTPUT_FILE"
echo "📊 文件大小: $(du -h "$OUTPUT_FILE" | cut -f1)"
echo ""
echo "接收者使用方法:"
echo "1. 解压文件"
echo "2. 创建虚拟环境: python3 -m venv venv"
echo "3. 激活虚拟环境: source venv/bin/activate"
echo "4. 安装依赖: pip install -r requirements.txt"
echo "5. 运行项目: python drawio.py"

#!/usr/bin/env python3
"""
运行所有 Phase 1 学习代码
"""

import subprocess
import sys
from pathlib import Path

# 课程列表
courses = [
    "01_syntax_basics.py",
    "02_data_structures.py",
    "03_functional_programming.py",
    "04_modern_python_types.py",
    "06_object_oriented_programming.py",
    "07_exception_handling_files.py",
    # "08_data_processing_preview.py",  # 需要安装 pandas 和 numpy
]

def run_course(filename: str) -> bool:
    """运行单个课程"""
    print(f"\n{'=' * 60}")
    print(f"🚀 运行: {filename}")
    print(f"{'=' * 60}\n")
    
    try:
        result = subprocess.run(
            [sys.executable, filename],
            cwd=Path(__file__).parent,
            capture_output=False,
            text=True
        )
        
        if result.returncode == 0:
            print(f"\n✅ {filename} 运行成功")
            return True
        else:
            print(f"\n❌ {filename} 运行失败 (退出码: {result.returncode})")
            return False
    except Exception as e:
        print(f"\n❌ {filename} 运行出错: {e}")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("Phase 1 Python 基础学习 - 全部课程")
    print("=" * 60)
    
    success_count = 0
    fail_count = 0
    
    for course in courses:
        if run_course(course):
            success_count += 1
        else:
            fail_count += 1
        
        # 暂停一下，让输出更清晰
        input("\n按 Enter 继续下一课...")
    
    # 总结
    print("\n" + "=" * 60)
    print("📊 运行总结")
    print("=" * 60)
    print(f"✅ 成功: {success_count} 个课程")
    print(f"❌ 失败: {fail_count} 个课程")
    print(f"📚 总计: {len(courses)} 个课程")
    print("=" * 60)

if __name__ == "__main__":
    main()

# 注意: 运行此脚本需要安装 pandas 和 numpy
# pip install pandas numpy

import sys

try:
    import pandas as pd
    import numpy as np
except ImportError:
    print("Error: pandas or numpy not installed.")
    print("Please run: pip install pandas numpy")
    sys.exit(1)

print("--- NumPy Basics ---")
# 创建数组
arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")
print(f"Mean: {np.mean(arr)}")
print(f"Max: {np.max(arr)}")

print("\n--- Pandas Basics ---")
# 创建 DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}
df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nSelect specific column (Age):")
print(df["Age"])

print("\nFilter data (Age > 28):")
print(df[df["Age"] > 28])

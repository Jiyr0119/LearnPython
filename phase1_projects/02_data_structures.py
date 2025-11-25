"""
第二课：数据结构
涵盖：列表、元组、字典、集合、推导式
"""

print("=" * 50)
print("第二课：数据结构")
print("=" * 50)

# ========================================
# 1. 列表 (List) - 可变序列
# ========================================
print("\n【1. 列表 (List)】")

# 创建列表
fruits = ["apple", "banana", "cherry"]
print(f"原始列表: {fruits}")

# 添加元素
fruits.append("date")           # 末尾添加
fruits.insert(1, "avocado")     # 指定位置插入
print(f"添加后: {fruits}")

# 访问元素
print(f"第一个元素: {fruits[0]}")
print(f"最后一个元素: {fruits[-1]}")
print(f"切片 [1:3]: {fruits[1:3]}")

# 修改元素
fruits[0] = "apricot"
print(f"修改后: {fruits}")

# 删除元素
fruits.remove("avocado")        # 按值删除
popped = fruits.pop()           # 删除并返回最后一个
print(f"删除后: {fruits}, 弹出的元素: {popped}")

# 列表方法
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\n数字列表: {numbers}")
print(f"  长度: {len(numbers)}")
print(f"  最大值: {max(numbers)}")
print(f"  最小值: {min(numbers)}")
print(f"  求和: {sum(numbers)}")
print(f"  排序后: {sorted(numbers)}")
print(f"  元素1出现次数: {numbers.count(1)}")
print(f"  元素4的索引: {numbers.index(4)}")

# 列表遍历
print("\n遍历列表:")
for i, fruit in enumerate(fruits, start=1):
    print(f"  {i}. {fruit}")

# ========================================
# 2. 元组 (Tuple) - 不可变序列
# ========================================
print("\n【2. 元组 (Tuple)】")

# 创建元组
coordinates = (10, 20)
rgb_color = (255, 128, 0)
single_item = (42,)  # 单元素元组需要逗号

print(f"坐标: {coordinates}")
print(f"RGB颜色: {rgb_color}")
print(f"单元素元组: {single_item}")

# 元组解包
x, y = coordinates
r, g, b = rgb_color
print(f"解包坐标: x={x}, y={y}")
print(f"解包颜色: R={r}, G={g}, B={b}")

# 元组不可变性
# coordinates[0] = 15  # ❌ 这行会报错！

# 元组的优势：作为字典的键
locations = {
    (0, 0): "原点",
    (1, 0): "东",
    (0, 1): "北"
}
print(f"位置字典: {locations}")
print(f"坐标(1,0)的位置: {locations[(1, 0)]}")

# ========================================
# 3. 字典 (Dictionary) - 键值对
# ========================================
print("\n【3. 字典 (Dictionary)】")

# 创建字典
user = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
    "skills": ["Python", "JavaScript", "SQL"]
}

print(f"用户信息: {user}")

# 访问元素
print(f"姓名: {user['name']}")
print(f"技能: {user['skills']}")

# 安全访问 (使用 get)
print(f"城市: {user.get('city', '未设置')}")  # 不存在时返回默认值

# 添加/修改
user["city"] = "Beijing"
user["age"] = 31
print(f"更新后: {user}")

# 删除
del user["email"]
print(f"删除email后: {user}")

# 字典方法
print(f"\n字典方法:")
print(f"  所有键: {list(user.keys())}")
print(f"  所有值: {list(user.values())}")
print(f"  所有键值对: {list(user.items())}")

# 遍历字典
print("\n遍历字典:")
for key, value in user.items():
    print(f"  {key}: {value}")

# 字典合并 (Python 3.9+)
defaults = {"theme": "dark", "language": "zh-CN"}
user_settings = {**defaults, **user}  # 展开运算符
print(f"合并后的设置: {user_settings}")

# ========================================
# 4. 集合 (Set) - 无序不重复
# ========================================
print("\n【4. 集合 (Set)】")

# 创建集合
numbers = {1, 2, 2, 3, 3, 3, 4, 5}
print(f"集合 (自动去重): {numbers}")

# 集合操作
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")
print(f"  并集: {set_a | set_b}")
print(f"  交集: {set_a & set_b}")
print(f"  差集 (A-B): {set_a - set_b}")
print(f"  对称差集: {set_a ^ set_b}")

# 集合方法
set_a.add(6)
set_a.remove(1)
print(f"修改后的 Set A: {set_a}")

# 实用案例：去重
tags = ["python", "coding", "python", "tutorial", "coding"]
unique_tags = list(set(tags))
print(f"\n标签去重: {tags} -> {unique_tags}")

# ========================================
# 5. 推导式 (Comprehensions)
# ========================================
print("\n【5. 推导式 - Pythonic 写法】")

# 列表推导式
squares = [x**2 for x in range(10)]
print(f"平方数列表: {squares}")

# 带条件的列表推导式
evens = [x for x in range(20) if x % 2 == 0]
print(f"偶数列表: {evens}")

# 字典推导式
fruits_list = ["apple", "banana", "cherry", "date"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits_list}
print(f"水果长度字典: {fruit_lengths}")

# 集合推导式
word = "hello"
unique_chars = {char for char in word}
print(f"'{word}' 的唯一字符: {unique_chars}")

# 嵌套推导式 (创建矩阵)
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"\n乘法表矩阵:")
for row in matrix:
    print(f"  {row}")

# 实用案例：数据转换
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

# 提取所有分数
scores = [student["score"] for student in students]
print(f"\n所有分数: {scores}")

# 筛选及格学生
passed = [s["name"] for s in students if s["score"] >= 80]
print(f"及格学生: {passed}")

# 创建姓名-分数映射
score_map = {s["name"]: s["score"] for s in students}
print(f"分数映射: {score_map}")

print("\n" + "=" * 50)
print("✅ 第二课完成！")
print("=" * 50)

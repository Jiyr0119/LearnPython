# 1. 列表 (List) - 可变序列
fruits = ["apple", "banana", "cherry"]
fruits.append("date")       # 添加
print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")

# 2. 元组 (Tuple) - 不可变序列
coordinates = (10, 20)
# coordinates[0] = 15  # 这行会报错，因为元组不可变
print(f"Coordinates: {coordinates}")

# 3. 字典 (Dictionary) - 键值对
user = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "JS"]
}
print(f"User Name: {user['name']}")
user["location"] = "Wonderland" # 添加键值对
print(f"User Keys: {list(user.keys())}")

# 4. 集合 (Set) - 无序不重复
numbers = {1, 2, 2, 3, 3, 3}
print(f"Unique numbers: {numbers}") # 输出 {1, 2, 3}

# 5. 推导式 (Comprehensions) - Pythonic 的写法
# 列表推导式: 生成 0-9 的平方列表
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# 字典推导式: 将 fruits 列表转为 {fruit: length} 字典
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(f"Fruit Lengths: {fruit_lengths}")

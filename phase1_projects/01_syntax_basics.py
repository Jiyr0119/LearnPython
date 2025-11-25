"""
第一课：Python 语法基础
涵盖：变量、数据类型、运算符、条件语句、循环、输入输出
"""

print("=" * 50)
print("第一课：Python 语法基础")
print("=" * 50)

# ========================================
# 1. 变量与数据类型
# ========================================
print("\n【1. 变量与数据类型】")

# 基本数据类型
name = "Python Learner"  # 字符串 (str)
age = 25                 # 整数 (int)
height = 1.75           # 浮点数 (float)
is_student = True       # 布尔值 (bool)
nothing = None          # 空值 (NoneType)

print(f"姓名: {name}, 类型: {type(name).__name__}")
print(f"年龄: {age}, 类型: {type(age).__name__}")
print(f"身高: {height}, 类型: {type(height).__name__}")
print(f"是学生: {is_student}, 类型: {type(is_student).__name__}")
print(f"空值: {nothing}, 类型: {type(nothing).__name__}")

# 字符串操作
print(f"\n字符串操作示例:")
print(f"  大写: {name.upper()}")
print(f"  小写: {name.lower()}")
print(f"  长度: {len(name)}")
print(f"  分割: {name.split()}")

# ========================================
# 2. 运算符
# ========================================
print("\n【2. 运算符】")

# 算术运算符
a, b = 10, 3
print(f"算术运算 (a={a}, b={b}):")
print(f"  加法: {a} + {b} = {a + b}")
print(f"  减法: {a} - {b} = {a - b}")
print(f"  乘法: {a} * {b} = {a * b}")
print(f"  除法: {a} / {b} = {a / b:.2f}")
print(f"  整除: {a} // {b} = {a // b}")
print(f"  取余: {a} % {b} = {a % b}")
print(f"  幂运算: {a} ** {b} = {a ** b}")

# 比较运算符
print(f"\n比较运算:")
print(f"  {a} > {b} = {a > b}")
print(f"  {a} == {b} = {a == b}")
print(f"  {a} != {b} = {a != b}")

# 逻辑运算符
is_adult = age >= 18
has_license = True
print(f"\n逻辑运算:")
print(f"  是成年人: {is_adult}")
print(f"  有驾照: {has_license}")
print(f"  可以开车: {is_adult and has_license}")
print(f"  至少满足一个: {is_adult or has_license}")
print(f"  取反: {not is_adult}")

# ========================================
# 3. 条件语句
# ========================================
print("\n【3. 条件语句】")

score = 85
print(f"分数: {score}")

if score >= 90:
    grade = "A - 优秀"
elif score >= 80:
    grade = "B - 良好"
elif score >= 70:
    grade = "C - 中等"
elif score >= 60:
    grade = "D - 及格"
else:
    grade = "F - 不及格"

print(f"等级: {grade}")

# 三元表达式 (简洁写法)
status = "成年人" if age >= 18 else "未成年人"
print(f"状态: {status}")

# ========================================
# 4. 循环语句
# ========================================
print("\n【4. 循环语句】")

# for 循环
print("for 循环 - 数字 1 到 5:")
for i in range(1, 6):
    print(f"  {i}", end=" ")
print()

# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
print("\nfor 循环 - 遍历列表:")
for fruit in fruits:
    print(f"  我喜欢{fruit}")

# enumerate - 同时获取索引和值
print("\nenumerate - 带索引遍历:")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")

# while 循环
print("\nwhile 循环 - 倒计时:")
count = 3
while count > 0:
    print(f"  {count}...")
    count -= 1
print("  发射! 🚀")

# break 和 continue
print("\nbreak 和 continue 示例:")
for i in range(1, 11):
    if i == 5:
        print(f"  跳过 {i} (continue)")
        continue
    if i == 8:
        print(f"  在 {i} 处停止 (break)")
        break
    print(f"  {i}", end=" ")
print()

# ========================================
# 5. 输入/输出操作
# ========================================
print("\n【5. 输入/输出操作】")

# 格式化输出
pi = 3.14159265359
print(f"格式化输出示例:")
print(f"  默认: {pi}")
print(f"  保留2位小数: {pi:.2f}")
print(f"  保留4位小数: {pi:.4f}")
print(f"  科学计数法: {pi:.2e}")

# 对齐输出
print(f"\n表格输出示例:")
print(f"{'姓名':<10} {'年龄':>5} {'城市':^10}")
print("-" * 30)
print(f"{'Alice':<10} {25:>5} {'北京':^10}")
print(f"{'Bob':<10} {30:>5} {'上海':^10}")
print(f"{'Charlie':<10} {35:>5} {'深圳':^10}")

# 输入操作 (注释掉，避免交互式运行时阻塞)
# print("\n输入操作示例:")
# user_name = input("请输入你的名字: ")
# user_age = int(input("请输入你的年龄: "))
# print(f"你好, {user_name}! 你今年 {user_age} 岁。")

print("\n" + "=" * 50)
print("✅ 第一课完成！")
print("=" * 50)

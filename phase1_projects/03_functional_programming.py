"""
第三课：函数式编程
涵盖：函数定义、参数传递、Lambda、map/filter/reduce、生成器、装饰器
"""

print("=" * 50)
print("第三课：函数式编程")
print("=" * 50)

# ========================================
# 1. 函数定义与参数
# ========================================
print("\n【1. 函数定义与参数】")

# 基本函数
def greet(name, greeting="Hello"):
    """
    问候函数
    :param name: 姓名
    :param greeting: 问候语 (默认: Hello)
    :return: 问候字符串
    """
    return f"{greeting}, {name}!"

print(greet("World"))
print(greet("Python", greeting="Hi"))

# 位置参数、关键字参数、默认参数
def create_user(username, email, age=18, is_active=True):
    return {
        "username": username,
        "email": email,
        "age": age,
        "is_active": is_active
    }

user1 = create_user("alice", "alice@example.com")
user2 = create_user("bob", "bob@example.com", age=25, is_active=False)
print(f"\n用户1: {user1}")
print(f"用户2: {user2}")

# *args 和 **kwargs
def calculate_sum(*numbers):
    """接收任意数量的位置参数"""
    return sum(numbers)

def print_info(**kwargs):
    """接收任意数量的关键字参数"""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print(f"\n求和: {calculate_sum(1, 2, 3, 4, 5)}")
print("用户信息:")
print_info(name="Alice", age=30, city="Beijing")

# 返回多个值
def get_stats(numbers):
    """返回统计信息"""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

min_val, max_val, avg_val = get_stats([10, 20, 30, 40, 50])
print(f"\n统计: 最小={min_val}, 最大={max_val}, 平均={avg_val}")

# ========================================
# 2. Lambda 表达式 (匿名函数)
# ========================================
print("\n【2. Lambda 表达式】")

# 基本 Lambda
add = lambda x, y: x + y
multiply = lambda x, y: x * y
print(f"5 + 3 = {add(5, 3)}")
print(f"5 * 3 = {multiply(5, 3)}")

# Lambda 用于排序
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

# 按分数排序
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print(f"\n按分数排序:")
for s in sorted_students:
    print(f"  {s['name']}: {s['score']}")

# ========================================
# 3. 高阶函数 (map, filter, reduce)
# ========================================
print("\n【3. 高阶函数】")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map: 对每个元素应用函数
doubled = list(map(lambda x: x * 2, numbers))
print(f"原始: {numbers}")
print(f"翻倍: {doubled}")

# filter: 过滤元素
evens = list(filter(lambda x: x % 2 == 0, numbers))
odds = list(filter(lambda x: x % 2 == 1, numbers))
print(f"偶数: {evens}")
print(f"奇数: {odds}")

# reduce: 累积计算 (需要导入)
from functools import reduce

# 计算乘积
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(f"\n1到5的乘积: {product}")

# 找最大值
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(f"最大值: {max_value}")

# 实用案例：链式操作
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
)
print(f"偶数的平方和: {result}")  # 2²+4²+6²+8²+10² = 220

# ========================================
# 4. 生成器 (Generator)
# ========================================
print("\n【4. 生成器 - 节省内存】")

# 生成器函数
def fibonacci(n):
    """生成斐波那契数列"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("斐波那契数列 (前10项):")
for num in fibonacci(10):
    print(num, end=" ")
print()

# 生成器表达式
squares_gen = (x**2 for x in range(10))
print(f"\n平方数生成器: {list(squares_gen)}")

# 实用案例：读取大文件
def read_large_file(filename):
    """逐行读取大文件 (模拟)"""
    lines = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5"]
    for line in lines:
        yield line.strip()

print("\n模拟读取文件:")
for line in read_large_file("dummy.txt"):
    print(f"  {line}")

# ========================================
# 5. 装饰器 (Decorator)
# ========================================
print("\n【5. 装饰器 - 函数增强】")

# 简单装饰器
def timer_decorator(func):
    """计时装饰器"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  [{func.__name__}] 执行时间: {(end - start) * 1000:.2f}ms")
        return result
    return wrapper

@timer_decorator
def slow_function():
    """模拟耗时操作"""
    import time
    time.sleep(0.1)
    return "完成"

print("调用装饰器函数:")
result = slow_function()

# 带参数的装饰器
def repeat(times):
    """重复执行装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello(name):
    print(f"  Hello, {name}!")
    return "Done"

print("\n重复执行3次:")
say_hello("Python")

# ========================================
# 6. 闭包 (Closure)
# ========================================
print("\n【6. 闭包】")

def make_multiplier(factor):
    """创建乘法器"""
    def multiplier(x):
        return x * factor
    return multiplier

times_2 = make_multiplier(2)
times_10 = make_multiplier(10)

print(f"5 * 2 = {times_2(5)}")
print(f"5 * 10 = {times_10(5)}")

# 实用案例：计数器
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter1 = make_counter()
counter2 = make_counter()

print(f"\n计数器1: {counter1()}, {counter1()}, {counter1()}")
print(f"计数器2: {counter2()}, {counter2()}")

# ========================================
# 7. 偏函数 (Partial Function)
# ========================================
print("\n【7. 偏函数】")

from functools import partial

# 基础函数
def power(base, exponent):
    return base ** exponent

# 创建偏函数
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(f"5的平方: {square(5)}")
print(f"5的立方: {cube(5)}")

# 实用案例：日志函数
def log(message, level="INFO"):
    print(f"[{level}] {message}")

log_error = partial(log, level="ERROR")
log_warning = partial(log, level="WARNING")

print("\n日志示例:")
log("普通消息")
log_error("这是错误")
log_warning("这是警告")

print("\n" + "=" * 50)
print("✅ 第三课完成！")
print("=" * 50)

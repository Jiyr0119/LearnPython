# 1. 函数定义
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("World"))
print(greet("Python", greeting="Hi"))

# 2. Lambda 表达式 (匿名函数)
add = lambda x, y: x + y
print(f"5 + 3 = {add(5, 3)}")

# 3. 高阶函数 (map, filter)
numbers = [1, 2, 3, 4, 5, 6]

# map: 对每个元素应用函数
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")

# filter: 过滤元素
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# 4. 生成器 (Generator) - 节省内存
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Fibonacci sequence:")
for num in fibonacci(6):
    print(num, end=" ")
print() # 换行

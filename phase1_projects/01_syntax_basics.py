# 1. 变量与数据类型
name = "Python Learner"  # 字符串
age = 25                 # 整数
height = 1.75           # 浮点数
is_student = True       # 布尔值

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")

# 2. 运算符
result = 10 + 5 * 2      # 算术运算符
is_adult = age >= 18     # 比较运算符
can_drive = is_adult and True # 逻辑运算符

print(f"Result: {result}")
print(f"Can drive: {can_drive}")

# 3. 条件语句
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(f"Score: {score}, Grade: {grade}")

# 4. 循环语句
print("Counting to 3:")
for i in range(1, 4):    # for 循环
    print(f"  Count: {i}")

count = 3
print("Countdown:")
while count > 0:         # while 循环
    print(f"  {count}")
    count -= 1
print("Blastoff!")

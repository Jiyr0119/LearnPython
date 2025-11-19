"""
计算器程序
实现基本的加减乘除运算
"""

def add(x, y):
    """加法函数"""
    return x + y

def subtract(x, y):
    """减法函数"""
    return x - y

def multiply(x, y):
    """乘法函数"""
    return x * y

def divide(x, y):
    """除法函数"""
    if y == 0:
        return "错误：除数不能为零"
    return x / y

def calculator():
    """主计算器函数"""
    print("欢迎使用简单计算器")
    print("支持的操作：+（加）、-（减）、*（乘）、/（除）")
    
    while True:
        # 获取用户输入
        num1 = input("请输入第一个数字（或输入 'q' 退出）: ")
        if num1.lower() == 'q':
            print("感谢使用计算器，再见！")
            break
            
        try:
            num1 = float(num1)
        except ValueError:
            print("请输入有效的数字！")
            continue
            
        operator = input("请输入操作符 (+, -, *, /): ")
        if operator not in ['+', '-', '*', '/']:
            print("无效的操作符，请重新输入！")
            continue
            
        num2 = input("请输入第二个数字: ")
        try:
            num2 = float(num2)
        except ValueError:
            print("请输入有效的数字！")
            continue
            
        # 执行计算
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
            
        # 显示结果
        print(f"结果: {num1} {operator} {num2} = {result}\n")

if __name__ == "__main__":
    calculator()
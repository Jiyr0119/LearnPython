"""
简单的密码生成器程序
根据指定规则生成随机密码
"""

import random
import string

def generate_password(length=12, include_uppercase=True, include_lowercase=True, 
                     include_digits=True, include_symbols=True):
    """
    生成随机密码
    
    参数:
    length: 密码长度
    include_uppercase: 是否包含大写字母
    include_lowercase: 是否包含小写字母
    include_digits: 是否包含数字
    include_symbols: 是否包含特殊符号
    """
    
    # 构建字符集
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # 检查字符集是否为空
    if not characters:
        raise ValueError("至少需要选择一种字符类型")
    
    # 生成密码
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    """获取用户密码偏好设置"""
    print("密码生成器设置:")
    
    # 获取密码长度
    while True:
        try:
            length = int(input("请输入密码长度 (默认12): ") or 12)
            if length <= 0:
                print("密码长度必须大于0")
                continue
            break
        except ValueError:
            print("请输入有效的数字")
    
    # 获取字符类型偏好
    include_uppercase = input("是否包含大写字母? (Y/n): ").lower() != 'n'
    include_lowercase = input("是否包含小写字母? (Y/n): ").lower() != 'n'
    include_digits = input("是否包含数字? (Y/n): ").lower() != 'n'
    include_symbols = input("是否包含特殊符号? (Y/n): ").lower() != 'n'
    
    return length, include_uppercase, include_lowercase, include_digits, include_symbols

def main():
    """主程序"""
    print("欢迎使用密码生成器")
    
    while True:
        try:
            # 获取用户设置
            length, uppercase, lowercase, digits, symbols = get_user_preferences()
            
            # 生成密码
            password = generate_password(length, uppercase, lowercase, digits, symbols)
            
            # 显示结果
            print(f"\n生成的密码: {password}")
            
            # 询问是否重新生成
            again = input("\n是否需要重新生成密码? (y/N): ").lower()
            if again != 'y':
                break
                
        except ValueError as e:
            print(f"错误: {e}")
        except KeyboardInterrupt:
            print("\n程序已退出")
            break
    
    print("感谢使用密码生成器！")

if __name__ == "__main__":
    main()
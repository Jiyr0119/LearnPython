"""
第六课：异常处理与文件操作
涵盖：try-except、自定义异常、文件读写、上下文管理器、JSON/CSV处理
"""

print("=" * 50)
print("第六课：异常处理与文件操作")
print("=" * 50)

# ========================================
# 1. 基础异常处理
# ========================================
print("\n【1. 基础异常处理】")

def divide(a: float, b: float) -> float:
    """除法运算"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("  ❌ 错误：除数不能为0")
        return 0.0
    except TypeError:
        print("  ❌ 错误：参数类型错误")
        return 0.0

print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")

# ========================================
# 2. 多重异常处理
# ========================================
print("\n【2. 多重异常处理】")

def safe_convert(value: str) -> int:
    """安全转换字符串为整数"""
    try:
        return int(value)
    except ValueError:
        print(f"  ❌ '{value}' 不是有效的整数")
        return 0
    except Exception as e:
        print(f"  ❌ 未知错误: {e}")
        return 0

print(f"转换 '123': {safe_convert('123')}")
print(f"转换 'abc': {safe_convert('abc')}")

# ========================================
# 3. try-except-else-finally
# ========================================
print("\n【3. try-except-else-finally】")

def process_file(filename: str) -> None:
    """处理文件 (演示完整异常处理)"""
    print(f"  处理文件: {filename}")
    try:
        # 模拟文件操作
        if filename == "error.txt":
            raise FileNotFoundError("文件不存在")
        print(f"    ✅ 文件打开成功")
    except FileNotFoundError as e:
        print(f"    ❌ 错误: {e}")
    else:
        print(f"    ✅ 文件处理完成")
    finally:
        print(f"    🔒 清理资源")

process_file("data.txt")
print()
process_file("error.txt")

# ========================================
# 4. 自定义异常
# ========================================
print("\n【4. 自定义异常】")

class InsufficientFundsError(Exception):
    """余额不足异常"""
    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount
        super().__init__(f"余额不足：当前余额 ¥{balance:.2f}，需要 ¥{amount:.2f}")

class InvalidAmountError(Exception):
    """无效金额异常"""
    pass

class BankAccount:
    """银行账户 (带异常处理)"""
    
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
    
    def withdraw(self, amount: float) -> None:
        """取款"""
        if amount <= 0:
            raise InvalidAmountError("取款金额必须大于0")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        
        self.balance -= amount
        print(f"  ✅ 取款成功：¥{amount:.2f}，余额：¥{self.balance:.2f}")

account = BankAccount("Alice", 1000.0)

try:
    account.withdraw(500)
    account.withdraw(800)  # 余额不足
except InsufficientFundsError as e:
    print(f"  ❌ {e}")
except InvalidAmountError as e:
    print(f"  ❌ {e}")

# ========================================
# 5. 文件读写 - 文本文件
# ========================================
print("\n【5. 文件读写 - 文本文件】")

import os
import tempfile

# 创建临时目录
temp_dir = tempfile.mkdtemp()
file_path = os.path.join(temp_dir, "example.txt")

# 写入文件
print(f"写入文件: {file_path}")
try:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("第一行\n")
        f.write("第二行\n")
        f.write("第三行\n")
    print("  ✅ 文件写入成功")
except IOError as e:
    print(f"  ❌ 写入失败: {e}")

# 读取文件
print("\n读取文件:")
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"  内容:\n{content}")
except FileNotFoundError:
    print("  ❌ 文件不存在")
except IOError as e:
    print(f"  ❌ 读取失败: {e}")

# 逐行读取
print("逐行读取:")
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, start=1):
            print(f"  第{i}行: {line.strip()}")
except IOError as e:
    print(f"  ❌ 读取失败: {e}")

# ========================================
# 6. JSON 文件处理
# ========================================
print("\n【6. JSON 文件处理】")

import json

# 准备数据
users_data = [
    {"id": 1, "name": "Alice", "age": 30, "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "age": 25, "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "age": 35, "email": "charlie@example.com"}
]

json_file = os.path.join(temp_dir, "users.json")

# 写入 JSON
print(f"写入 JSON: {json_file}")
try:
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(users_data, f, ensure_ascii=False, indent=2)
    print("  ✅ JSON 写入成功")
except IOError as e:
    print(f"  ❌ 写入失败: {e}")

# 读取 JSON
print("\n读取 JSON:")
try:
    with open(json_file, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
        print("  用户列表:")
        for user in loaded_data:
            print(f"    - {user['name']} ({user['age']}岁): {user['email']}")
except FileNotFoundError:
    print("  ❌ 文件不存在")
except json.JSONDecodeError as e:
    print(f"  ❌ JSON 解析失败: {e}")
except IOError as e:
    print(f"  ❌ 读取失败: {e}")

# ========================================
# 7. CSV 文件处理
# ========================================
print("\n【7. CSV 文件处理】")

import csv

csv_file = os.path.join(temp_dir, "products.csv")

# 写入 CSV
print(f"写入 CSV: {csv_file}")
products = [
    ["ID", "名称", "价格", "库存"],
    [1, "笔记本电脑", 5999.00, 10],
    [2, "鼠标", 99.00, 50],
    [3, "键盘", 299.00, 30]
]

try:
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(products)
    print("  ✅ CSV 写入成功")
except IOError as e:
    print(f"  ❌ 写入失败: {e}")

# 读取 CSV
print("\n读取 CSV:")
try:
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                print(f"  表头: {', '.join(row)}")
            else:
                print(f"  {row[0]}: {row[1]} - ¥{row[2]} (库存: {row[3]})")
except FileNotFoundError:
    print("  ❌ 文件不存在")
except IOError as e:
    print(f"  ❌ 读取失败: {e}")

# 使用 DictReader (更方便)
print("\n使用 DictReader 读取:")
try:
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"  {row['名称']}: ¥{row['价格']}")
except FileNotFoundError:
    print("  ❌ 文件不存在")
except IOError as e:
    print(f"  ❌ 读取失败: {e}")

# ========================================
# 8. 上下文管理器
# ========================================
print("\n【8. 上下文管理器】")

class FileLogger:
    """文件日志记录器 (自定义上下文管理器)"""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        """进入上下文"""
        print(f"  📂 打开日志文件: {self.filename}")
        self.file = open(self.filename, 'w', encoding='utf-8')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文"""
        if self.file:
            self.file.close()
            print(f"  🔒 关闭日志文件")
        
        if exc_type is not None:
            print(f"  ❌ 发生异常: {exc_type.__name__}: {exc_val}")
        
        return False  # 不抑制异常

log_file = os.path.join(temp_dir, "app.log")

# 使用自定义上下文管理器
with FileLogger(log_file) as f:
    f.write("应用启动\n")
    f.write("处理请求\n")
    f.write("应用关闭\n")

print("\n日志内容:")
with open(log_file, 'r', encoding='utf-8') as f:
    print(f.read())

# ========================================
# 9. 实用案例：配置文件管理
# ========================================
print("\n【9. 实用案例：配置文件管理】")

class ConfigManager:
    """配置文件管理器"""
    
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.config = {}
    
    def load(self) -> None:
        """加载配置"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            print(f"  ✅ 配置加载成功")
        except FileNotFoundError:
            print(f"  ⚠️  配置文件不存在，使用默认配置")
            self.config = self._get_default_config()
            self.save()
        except json.JSONDecodeError as e:
            print(f"  ❌ 配置文件格式错误: {e}")
            self.config = self._get_default_config()
    
    def save(self) -> None:
        """保存配置"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=2)
            print(f"  ✅ 配置保存成功")
        except IOError as e:
            print(f"  ❌ 配置保存失败: {e}")
    
    def get(self, key: str, default=None):
        """获取配置项"""
        return self.config.get(key, default)
    
    def set(self, key: str, value) -> None:
        """设置配置项"""
        self.config[key] = value
    
    def _get_default_config(self) -> dict:
        """获取默认配置"""
        return {
            "app_name": "MyApp",
            "version": "1.0.0",
            "debug": False,
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "mydb"
            }
        }

config_file = os.path.join(temp_dir, "config.json")
config = ConfigManager(config_file)

# 加载配置
config.load()

# 读取配置
print(f"\n应用名称: {config.get('app_name')}")
print(f"版本: {config.get('version')}")
print(f"数据库: {config.get('database')}")

# 修改配置
config.set('debug', True)
config.set('max_connections', 100)
config.save()

# 清理临时文件
import shutil
shutil.rmtree(temp_dir)
print(f"\n🗑️  已清理临时文件: {temp_dir}")

print("\n" + "=" * 50)
print("✅ 第六课完成！")
print("=" * 50)

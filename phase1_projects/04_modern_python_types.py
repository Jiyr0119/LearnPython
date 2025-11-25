"""
第四课：现代 Python 类型提示 (Type Hinting)
涵盖：基础类型、泛型、Optional、Union、Callable、TypedDict
"""

from typing import List, Dict, Optional, Union, Tuple, Set, Callable, Any
from typing import TypedDict  # Python 3.8+

print("=" * 50)
print("第四课：现代 Python 类型提示")
print("=" * 50)

# ========================================
# 1. 基础类型提示
# ========================================
print("\n【1. 基础类型提示】")

def calculate_area(radius: float) -> float:
    """计算圆的面积"""
    return 3.14159 * radius * radius

def greet_user(name: str, age: int) -> str:
    """问候用户"""
    return f"Hello, {name}! You are {age} years old."

print(f"圆面积 (r=2.5): {calculate_area(2.5):.2f}")
print(greet_user("Alice", 30))

# 变量类型注解
username: str = "Bob"
user_age: int = 25
is_active: bool = True
score: float = 95.5

print(f"\n用户: {username}, 年龄: {user_age}, 活跃: {is_active}, 分数: {score}")

# ========================================
# 2. 复杂类型提示 (List, Dict, Tuple, Set)
# ========================================
print("\n【2. 复杂类型提示】")

def process_scores(scores: List[int]) -> Dict[str, float]:
    """处理分数列表，返回统计信息"""
    if not scores:
        return {"average": 0.0, "max": 0.0, "min": 0.0}
    return {
        "average": sum(scores) / len(scores),
        "max": float(max(scores)),
        "min": float(min(scores))
    }

result = process_scores([80, 90, 95, 88, 92])
print(f"分数统计: {result}")

# 元组类型
def get_user_info() -> Tuple[str, int, str]:
    """返回用户信息 (姓名, 年龄, 城市)"""
    return ("Alice", 30, "Beijing")

name, age, city = get_user_info()
print(f"\n用户信息: {name}, {age}岁, 来自{city}")

# 集合类型
def get_unique_tags(articles: List[Dict[str, Any]]) -> Set[str]:
    """提取所有唯一标签"""
    tags: Set[str] = set()
    for article in articles:
        tags.update(article.get("tags", []))
    return tags

articles = [
    {"title": "Python入门", "tags": ["python", "tutorial"]},
    {"title": "Web开发", "tags": ["python", "web", "flask"]},
]
print(f"所有标签: {get_unique_tags(articles)}")

# ========================================
# 3. Optional 类型 (可能为 None)
# ========================================
print("\n【3. Optional 类型】")

def find_user(user_id: int) -> Optional[str]:
    """查找用户，可能返回 None"""
    users: Dict[int, str] = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return users.get(user_id)

user1 = find_user(1)
user99 = find_user(99)

print(f"用户1: {user1}")
print(f"用户99: {user99}")

# 处理 Optional 值
def get_user_display_name(user_id: int) -> str:
    """获取用户显示名称"""
    name = find_user(user_id)
    return name if name is not None else "未知用户"

print(f"显示名称: {get_user_display_name(1)}")
print(f"显示名称: {get_user_display_name(99)}")

# ========================================
# 4. Union 类型 (多种可能类型)
# ========================================
print("\n【4. Union 类型】")

def format_value(value: Union[int, float, str]) -> str:
    """格式化不同类型的值"""
    if isinstance(value, int):
        return f"整数: {value}"
    elif isinstance(value, float):
        return f"浮点数: {value:.2f}"
    else:
        return f"字符串: {value}"

print(format_value(42))
print(format_value(3.14159))
print(format_value("Hello"))

# Python 3.10+ 新语法: int | float | str (替代 Union)
# def format_value(value: int | float | str) -> str:
#     ...

# ========================================
# 5. Callable 类型 (函数类型)
# ========================================
print("\n【5. Callable 类型】")

def apply_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
    """应用指定的操作函数"""
    return operation(x, y)

def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

print(f"\n10 + 5 = {apply_operation(10, 5, add)}")
print(f"10 * 5 = {apply_operation(10, 5, multiply)}")

# 使用 Lambda
print(f"10 - 5 = {apply_operation(10, 5, lambda a, b: a - b)}")

# ========================================
# 6. TypedDict (结构化字典)
# ========================================
print("\n【6. TypedDict - 结构化字典】")

class UserDict(TypedDict):
    """用户字典类型定义"""
    id: int
    name: str
    email: str
    age: int
    is_active: bool

def create_user(name: str, email: str, age: int) -> UserDict:
    """创建用户字典"""
    return {
        "id": 1,
        "name": name,
        "email": email,
        "age": age,
        "is_active": True
    }

def display_user(user: UserDict) -> None:
    """显示用户信息"""
    print(f"  ID: {user['id']}")
    print(f"  姓名: {user['name']}")
    print(f"  邮箱: {user['email']}")
    print(f"  年龄: {user['age']}")
    print(f"  活跃: {user['is_active']}")

new_user = create_user("Alice", "alice@example.com", 30)
print("新用户:")
display_user(new_user)

# ========================================
# 7. 泛型与类型变量
# ========================================
print("\n【7. 泛型】")

from typing import TypeVar, Generic

T = TypeVar('T')

def get_first_element(items: List[T]) -> Optional[T]:
    """获取列表第一个元素"""
    return items[0] if items else None

numbers_list: List[int] = [1, 2, 3]
strings_list: List[str] = ["a", "b", "c"]
empty_list: List[int] = []

print(f"第一个数字: {get_first_element(numbers_list)}")
print(f"第一个字符串: {get_first_element(strings_list)}")
print(f"空列表: {get_first_element(empty_list)}")

# ========================================
# 8. Any 类型 (任意类型)
# ========================================
print("\n【8. Any 类型】")

def process_data(data: Any) -> str:
    """处理任意类型的数据"""
    return f"数据类型: {type(data).__name__}, 值: {data}"

print(process_data(42))
print(process_data("Hello"))
print(process_data([1, 2, 3]))
print(process_data({"key": "value"}))

# ========================================
# 9. 实用案例：API 响应处理
# ========================================
print("\n【9. 实用案例：API 响应】")

class APIResponse(TypedDict):
    """API 响应类型"""
    status: int
    message: str
    data: Optional[Dict[str, Any]]

def fetch_user_data(user_id: int) -> APIResponse:
    """模拟 API 请求"""
    if user_id > 0:
        return {
            "status": 200,
            "message": "Success",
            "data": {"id": user_id, "name": "Alice", "email": "alice@example.com"}
        }
    else:
        return {
            "status": 404,
            "message": "User not found",
            "data": None
        }

def handle_response(response: APIResponse) -> None:
    """处理 API 响应"""
    print(f"  状态码: {response['status']}")
    print(f"  消息: {response['message']}")
    if response['data']:
        print(f"  数据: {response['data']}")

print("成功响应:")
handle_response(fetch_user_data(1))

print("\n失败响应:")
handle_response(fetch_user_data(-1))

# ========================================
# 总结
# ========================================
print("\n" + "=" * 50)
print("✅ 第四课完成！")
print("=" * 50)
print("\n💡 提示:")
print("  - 类型提示主要用于静态分析 (如 mypy) 和 IDE 自动补全")
print("  - Python 运行时不会强制检查类型")
print("  - 使用类型提示是现代 Python 开发的最佳实践")
print("  - 对于 FastAPI 等框架，类型提示是必需的")
print("\n运行 mypy 检查类型:")
print("  $ mypy 04_modern_python_types.py")
print("=" * 50)

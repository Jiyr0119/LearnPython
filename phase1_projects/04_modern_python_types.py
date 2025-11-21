from typing import List, Dict, Optional

# 1. 基础类型提示
def calculate_area(radius: float) -> float:
    return 3.14159 * radius * radius

print(f"Area: {calculate_area(2.5)}")

# 2. 复杂类型提示 (List, Dict)
def process_scores(scores: List[int]) -> Dict[str, float]:
    if not scores:
        return {"average": 0.0}
    return {"average": sum(scores) / len(scores)}

print(process_scores([80, 90, 95]))

# 3. Optional 类型 (可能为 None)
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

user1 = find_user(1)
user99 = find_user(99)

print(f"User 1: {user1}")
print(f"User 99: {user99}")

# 注意: 类型提示主要用于静态分析(如mypy)和IDE自动补全，
# Python 运行时不会强制检查类型，但这是一个非常好的习惯！

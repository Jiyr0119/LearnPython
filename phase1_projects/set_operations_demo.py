"""
集合运算详解 - 可视化示例
"""

print("=" * 60)
print("集合运算详解")
print("=" * 60)

# 基础示例
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")

print("\n【1. 并集 (Union) - A | B】")
print(f"  结果: {set_a | set_b}")
print(f"  含义: 所有在 A 或 B 中的元素")
print(f"  等价: {set_a.union(set_b)}")

print("\n【2. 交集 (Intersection) - A & B】")
print(f"  结果: {set_a & set_b}")
print(f"  含义: 同时在 A 和 B 中的元素")
print(f"  等价: {set_a.intersection(set_b)}")

print("\n【3. 差集 (Difference) - A - B】")
print(f"  A - B: {set_a - set_b}")
print(f"  含义: 在 A 中但不在 B 中的元素")
print(f"  等价: {set_a.difference(set_b)}")
print(f"\n  B - A: {set_b - set_a}")
print(f"  含义: 在 B 中但不在 A 中的元素")
print(f"  注意: A - B ≠ B - A")

print("\n【4. 对称差集 (Symmetric Difference) - A ^ B】")
print(f"  结果: {set_a ^ set_b}")
print(f"  含义: 在 A 或 B 中，但不同时在两者中的元素")
print(f"  等价: {set_a.symmetric_difference(set_b)}")
print(f"  公式: (A - B) ∪ (B - A) = {(set_a - set_b) | (set_b - set_a)}")

# ============================================
# 实际应用案例
# ============================================

print("\n" + "=" * 60)
print("实际应用案例")
print("=" * 60)

# 案例 1: 课程选修
print("\n【案例 1: 课程选修】")
course_a = {"Alice", "Bob", "Charlie", "David"}
course_b = {"Bob", "Charlie", "Eve", "Frank"}

print(f"选修课程A的学生: {course_a}")
print(f"选修课程B的学生: {course_b}")
print(f"\n  至少选一门课: {course_a | course_b}")
print(f"  两门都选: {course_a & course_b}")
print(f"  只选A不选B: {course_a - course_b}")
print(f"  只选一门课: {course_a ^ course_b}")

# 案例 2: 标签系统
print("\n【案例 2: 文章标签】")
article1_tags = {"python", "programming", "tutorial", "beginner"}
article2_tags = {"python", "web", "flask", "tutorial"}

print(f"文章1标签: {article1_tags}")
print(f"文章2标签: {article2_tags}")
print(f"\n  所有标签: {article1_tags | article2_tags}")
print(f"  共同标签: {article1_tags & article2_tags}")
print(f"  文章1独有: {article1_tags - article2_tags}")
print(f"  不同的标签: {article1_tags ^ article2_tags}")

# 案例 3: 用户活跃度
print("\n【案例 3: 用户活跃度分析】")
yesterday_users = {"user1", "user2", "user3", "user5"}
today_users = {"user2", "user3", "user4", "user6"}

print(f"昨天在线: {yesterday_users}")
print(f"今天在线: {today_users}")
print(f"\n  总用户数: {yesterday_users | today_users}")
print(f"  连续在线: {yesterday_users & today_users}")
print(f"  昨天在线今天不在: {yesterday_users - today_users}")
print(f"  只在一天在线: {yesterday_users ^ today_users}")

# 案例 4: 权限管理
print("\n【案例 4: 权限管理】")
admin_permissions = {"read", "write", "delete", "admin"}
user_permissions = {"read", "write", "comment"}

print(f"管理员权限: {admin_permissions}")
print(f"普通用户权限: {user_permissions}")
print(f"\n  所有权限: {admin_permissions | user_permissions}")
print(f"  共同权限: {admin_permissions & user_permissions}")
print(f"  管理员独有: {admin_permissions - user_permissions}")

# ============================================
# 韦恩图可视化 (文本版)
# ============================================

print("\n" + "=" * 60)
print("韦恩图可视化 (文本版)")
print("=" * 60)

print("""
Set A = {1, 2, 3, 4, 5}
Set B = {4, 5, 6, 7, 8}

     ┌─────────────┐
     │   A only    │
     │  {1, 2, 3}  │
     │      ┌──────┼──────┐
     │      │ A∩B  │      │
     │      │{4,5} │      │
     └──────┼──────┘      │
            │   B only    │
            │  {6, 7, 8}  │
            └─────────────┘

并集 (A | B):     {1, 2, 3, 4, 5, 6, 7, 8}  ← 整个图
交集 (A & B):     {4, 5}                    ← 中间重叠部分
差集 (A - B):     {1, 2, 3}                 ← 只在左边
差集 (B - A):     {6, 7, 8}                 ← 只在右边
对称差集 (A ^ B): {1, 2, 3, 6, 7, 8}       ← 左边 + 右边 (去掉中间)
""")

print("=" * 60)
print("✅ 集合运算学习完成！")
print("=" * 60)

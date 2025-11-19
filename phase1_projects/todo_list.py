"""
待办事项列表程序
使用列表存储任务，实现添加、删除、查看功能
"""

# 全局任务列表
tasks = []

def show_tasks():
    """显示所有任务"""
    if not tasks:
        print("当前没有任务。")
    else:
        print("\n当前任务列表：")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("-" * 30)

def add_task():
    """添加新任务"""
    task = input("请输入新任务: ")
    if task:
        tasks.append(task)
        print(f"任务 '{task}' 已添加。")
    else:
        print("任务不能为空！")

def delete_task():
    """删除任务"""
    show_tasks()
    if not tasks:
        return
        
    try:
        index = int(input("请输入要删除的任务编号: ")) - 1
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            print(f"任务 '{deleted_task}' 已删除。")
        else:
            print("无效的任务编号！")
    except ValueError:
        print("请输入有效的数字！")

def main():
    """主程序"""
    print("欢迎使用待办事项列表程序")
    
    while True:
        print("\n请选择操作:")
        print("1. 查看任务")
        print("2. 添加任务")
        print("3. 删除任务")
        print("4. 退出程序")
        
        choice = input("请输入选项 (1-4): ")
        
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("感谢使用待办事项列表，再见！")
            break
        else:
            print("无效选项，请重新输入！")

if __name__ == "__main__":
    main()
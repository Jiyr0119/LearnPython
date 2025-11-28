# 第一阶段：巩固 Python 基础

作为从 前端全栈工程师 转型的开发者，你已经具备了一定的编程思维和经验。这一阶段的目标是快速掌握 Python 的核心语法和现代开发实践，为后续学习打下坚实基础。

## 学习内容

1. **Python 语法基础**
   - 变量与数据类型 (数字、字符串、布尔值)
   - 运算符 (算术、比较、逻辑)
   - 条件语句 (if/elif/else)
   - 循环语句 (for/while)
   - 输入/输出操作 (input/print)

2. **数据结构**
   - 列表 (List) - 创建、访问、修改、遍历
   - 元组 (Tuple) - 不可变序列
   - 字典 (Dictionary) - 键值对存储
   - 集合 (Set) - 无序不重复元素
   - 列表推导式、字典推导式

3. **函数式编程**
   - 函数定义与调用
   - 参数传递 (位置参数、关键字参数、默认参数)
   - 返回值
   - Lambda 表达式
   - map, filter, reduce 函数
   - 生成器与迭代器

4. **类型提示 (Type Hints)** - *现代 Python 开发的核心实践*
   - 基本类型提示: int, str, bool, float
   - 容器类型: List, Dict, Tuple, Set
   - 可选类型: Optional, Union
   - 函数类型提示
   - 变量类型提示
   - 类型检查工具: mypy

5. **测试实践** - *确保代码质量的基础*
   - 单元测试基础 (unittest, pytest)
   - 测试驱动开发 (TDD) 概念
   - 测试覆盖率
   - mock 对象使用
   - 参数化测试

6. **数据处理基础** (为AI/RAG做准备)
   - Pandas 库基础 (DataFrame, Series)
   - 数据读取与写入 (CSV, JSON, Excel)
   - 数据清洗与预处理
   - NumPy 基础 (数组操作)

7. **现代 Python 开发环境**
   - **虚拟环境管理**: venv (内置), poetry (推荐), conda (数据科学常用)
   - **包管理**: pip, requirements.txt, pyproject.toml
   - **代码质量工具**:
     - 格式化: black, isort
     - 静态分析: ruff (替代flake8和pylint), mypy (类型检查)
     - 预提交钩子: pre-commit
   - **项目结构**: 使用 pyproject.toml 统一管理项目依赖和配置

## 学习资源推荐

- **官方文档**: [Python 官方教程](https://docs.python.org/zh-cn/3/tutorial/index.html) - 最权威的学习资料
- **书籍**:
  - 《Python编程：从入门到实践》- 适合初学者，实践性强
  - 《流畅的Python》- 适合有一定基础的开发者，深入理解Python特性
  - 《Effective Python》- 现代Python最佳实践
- **在线教程**:
  - [Python官方文档](https://docs.python.org/zh-cn/3/)
  - [Real Python](https://realpython.com/) - 高质量Python教程
- **GitHub 项目**:
  - [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) - Python算法实现
  - [karan/Projects](https://github.com/karan/Projects) - Python实践项目

## 实践项目

完成以下小项目来检验学习成果：

1. **计算器程序** - 实现基本的加减乘除运算，使用类型提示
2. **待办事项列表** - 使用列表存储任务，实现添加、删除、查看功能，并编写单元测试
3. **单词计数器** - 读取文本文件，统计单词出现频率，使用类型提示和错误处理
4. **简单的密码生成器** - 根据指定规则生成随机密码，包含测试用例
5. **数据处理脚本** - 使用pandas处理CSV文件，进行数据分析和可视化，包含类型提示

## 学习建议

- 每天花1-2小时学习理论知识，并立即动手实践
- 多做练习题，如 LeetCode 上的简单题目
- 尝试用 Python 重写一些你之前用 JavaScript 写的小工具
- 加入 Python 学习社群，与其他学习者交流心得
- 每周进行自我评估，记录学习进度和难点
- 建立学习日志，记录每日学习内容和心得体会
- 在学习初期就建立良好的代码质量习惯：类型提示、测试、代码格式化
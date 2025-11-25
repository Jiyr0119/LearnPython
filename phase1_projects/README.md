# Phase 1 Python 基础学习 - 课程总览

本目录包含 Python 基础学习的系统化代码示例，按照从易到难的顺序组织。

## 📚 课程列表

### 01. Python 语法基础 (`01_syntax_basics.py`)
**学习内容：**
- 变量与数据类型 (str, int, float, bool, None)
- 运算符 (算术、比较、逻辑)
- 条件语句 (if/elif/else, 三元表达式)
- 循环语句 (for, while, break, continue, enumerate)
- 输入/输出操作 (格式化输出、对齐)

**关键概念：**
- f-string 格式化
- range() 函数
- enumerate() 带索引遍历

---

### 02. 数据结构 (`02_data_structures.py`)
**学习内容：**
- 列表 (List) - 创建、访问、修改、遍历、方法
- 元组 (Tuple) - 不可变序列、解包
- 字典 (Dictionary) - 键值对、方法、遍历
- 集合 (Set) - 去重、集合运算
- 推导式 (List/Dict/Set Comprehension)

**关键概念：**
- 列表方法: append, insert, remove, pop, sort
- 字典方法: get, keys, values, items
- 集合运算: 并集、交集、差集
- 推导式的高效写法

---

### 03. 函数式编程 (`03_functional_programming.py`)
**学习内容：**
- 函数定义与参数 (位置、关键字、默认、*args, **kwargs)
- Lambda 表达式
- 高阶函数 (map, filter, reduce)
- 生成器 (Generator) - yield, 生成器表达式
- 装饰器 (Decorator) - 函数增强
- 闭包 (Closure)
- 偏函数 (Partial Function)

**关键概念：**
- 函数是一等公民
- 惰性求值 (生成器)
- 装饰器语法糖 @decorator
- functools 模块

---

### 04. 现代 Python 类型提示 (`04_modern_python_types.py`)
**学习内容：**
- 基础类型注解 (str, int, float, bool)
- 复杂类型 (List, Dict, Tuple, Set)
- Optional 类型 (可能为 None)
- Union 类型 (多种可能类型)
- Callable 类型 (函数类型)
- TypedDict (结构化字典)
- 泛型 (Generic, TypeVar)
- Any 类型

**关键概念：**
- 类型提示用于静态分析和 IDE 支持
- mypy 类型检查工具
- FastAPI 等现代框架必需
- Python 3.10+ 新语法: `int | str`

---

### 05. 面向对象编程 (`06_object_oriented_programming.py`)
**学习内容：**
- 类与对象基础 (__init__, 实例属性/方法)
- 继承 (Inheritance) - super(), 方法重写
- 多态 (Polymorphism)
- 封装 (Encapsulation) - 私有属性
- 属性装饰器 (@property, @setter)
- 特殊方法 (Magic Methods) - __str__, __add__, __eq__ 等
- 类方法 (@classmethod) 和静态方法 (@staticmethod)

**关键概念：**
- 类属性 vs 实例属性
- 私有属性命名约定 (双下划线)
- 特殊方法实现运算符重载
- 实用案例：购物车系统

---

### 06. 异常处理与文件操作 (`07_exception_handling_files.py`)
**学习内容：**
- 基础异常处理 (try-except)
- 多重异常处理
- try-except-else-finally 完整结构
- 自定义异常
- 文本文件读写
- JSON 文件处理
- CSV 文件处理
- 上下文管理器 (with 语句, __enter__, __exit__)

**关键概念：**
- 异常类型: ValueError, FileNotFoundError, IOError
- with 语句自动资源管理
- json.dump/load, csv.reader/writer
- 实用案例：配置文件管理器

---

### 07. 数据处理预览 (`08_data_processing_preview.py`)
**学习内容：**
- NumPy 基础 (数组操作、统计函数)
- Pandas 基础 (DataFrame, Series)
- 数据筛选和处理

**关键概念：**
- 需要安装: `pip install pandas numpy`
- 为 AI/RAG 项目做准备
- 数据科学基础工具

---

## 🎯 学习路径建议

### 第 1 周：基础语法
- Day 1-2: 01_syntax_basics.py
- Day 3-4: 02_data_structures.py
- Day 5-7: 练习项目 (计算器、待办事项)

### 第 2 周：进阶特性
- Day 1-3: 03_functional_programming.py
- Day 4-5: 04_modern_python_types.py
- Day 6-7: 综合练习

### 第 3 周：面向对象与工程化
- Day 1-3: 06_object_oriented_programming.py
- Day 4-5: 07_exception_handling_files.py
- Day 6-7: 实战项目 (单词计数器、密码生成器)

### 第 4 周：数据处理
- Day 1-3: 08_data_processing_preview.py
- Day 4-7: 综合项目实战

---

## 🚀 运行代码

```bash
# 运行单个课程
python 01_syntax_basics.py

# 运行所有课程 (按顺序)
for file in 0{1..8}*.py; do
    echo "========== $file =========="
    python "$file"
    echo ""
done
```

---

## 📖 配套实践项目

在学习理论知识的同时，建议完成以下实践项目：

1. **calculator.py** - 计算器程序
2. **todo_list.py** - 待办事项列表
3. **word_counter.py** - 单词计数器
4. **password_generator.py** - 密码生成器

---

## 💡 学习建议

1. **循序渐进**: 按照 01-08 的顺序学习，不要跳跃
2. **动手实践**: 每学完一课，立即运行代码并修改实验
3. **做笔记**: 记录不理解的概念，及时查阅文档
4. **写代码**: 尝试自己实现类似功能，不要只看不写
5. **复习**: 定期回顾之前的内容，巩固记忆

---

## 🔗 相关资源

- **官方文档**: [Python 官方教程](https://docs.python.org/zh-cn/3/tutorial/)
- **类型检查**: `pip install mypy` → `mypy 04_modern_python_types.py`
- **代码格式化**: `pip install black` → `black *.py`
- **静态分析**: `pip install flake8` → `flake8 *.py`

---

## ✅ 学习检查清单

完成每一课后，确保你能够：

- [ ] 01: 能够使用各种运算符和控制流编写基础程序
- [ ] 02: 熟练使用列表、字典等数据结构解决问题
- [ ] 03: 理解并能编写高阶函数、装饰器、生成器
- [ ] 04: 能够为函数和变量添加正确的类型注解
- [ ] 05: 能够设计和实现面向对象的程序
- [ ] 06: 能够正确处理异常和进行文件操作
- [ ] 07: 能够使用 NumPy 和 Pandas 进行基础数据处理

---

**祝学习愉快！🎉**

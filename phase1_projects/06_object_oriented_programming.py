"""
第五课：面向对象编程 (OOP)
涵盖：类与对象、继承、多态、封装、特殊方法、属性装饰器
"""

print("=" * 50)
print("第五课：面向对象编程")
print("=" * 50)

# ========================================
# 1. 类与对象基础
# ========================================
print("\n【1. 类与对象基础】")

class Person:
    """人类"""
    
    # 类属性 (所有实例共享)
    species = "Homo sapiens"
    
    def __init__(self, name: str, age: int):
        """构造函数"""
        # 实例属性
        self.name = name
        self.age = age
    
    def greet(self) -> str:
        """实例方法"""
        return f"你好，我是 {self.name}，今年 {self.age} 岁"
    
    def celebrate_birthday(self) -> None:
        """过生日"""
        self.age += 1
        print(f"🎂 {self.name} 过生日了！现在 {self.age} 岁")

# 创建对象
alice = Person("Alice", 30)
bob = Person("Bob", 25)

print(alice.greet())
print(bob.greet())
print(f"物种: {Person.species}")

alice.celebrate_birthday()

# ========================================
# 2. 继承 (Inheritance)
# ========================================
print("\n【2. 继承】")

class Student(Person):
    """学生类 (继承自 Person)"""
    
    def __init__(self, name: str, age: int, student_id: str, major: str):
        # 调用父类构造函数
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major
        self.grades = []
    
    def add_grade(self, grade: float) -> None:
        """添加成绩"""
        self.grades.append(grade)
    
    def get_average(self) -> float:
        """计算平均分"""
        return sum(self.grades) / len(self.grades) if self.grades else 0.0
    
    def greet(self) -> str:
        """重写父类方法"""
        return f"你好，我是学生 {self.name}，学号 {self.student_id}，专业 {self.major}"

class Teacher(Person):
    """教师类 (继承自 Person)"""
    
    def __init__(self, name: str, age: int, subject: str, years_experience: int):
        super().__init__(name, age)
        self.subject = subject
        self.years_experience = years_experience
    
    def greet(self) -> str:
        """重写父类方法"""
        return f"你好，我是 {self.subject} 老师 {self.name}，有 {self.years_experience} 年教学经验"

# 使用继承
student = Student("Charlie", 20, "S001", "计算机科学")
teacher = Teacher("Dr. Smith", 45, "数学", 20)

print(student.greet())
student.add_grade(85)
student.add_grade(90)
student.add_grade(88)
print(f"平均分: {student.get_average():.2f}")

print(teacher.greet())

# ========================================
# 3. 多态 (Polymorphism)
# ========================================
print("\n【3. 多态】")

def introduce_person(person: Person) -> None:
    """介绍一个人 (多态)"""
    print(f"  {person.greet()}")

people = [
    Person("Alice", 30),
    Student("Bob", 22, "S002", "物理"),
    Teacher("Dr. Wang", 50, "化学", 25)
]

print("介绍所有人:")
for person in people:
    introduce_person(person)

# ========================================
# 4. 封装 (Encapsulation)
# ========================================
print("\n【4. 封装 - 私有属性】")

class BankAccount:
    """银行账户"""
    
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = balance  # 私有属性 (双下划线)
    
    def deposit(self, amount: float) -> None:
        """存款"""
        if amount > 0:
            self.__balance += amount
            print(f"存入 ¥{amount:.2f}，余额: ¥{self.__balance:.2f}")
        else:
            print("存款金额必须大于0")
    
    def withdraw(self, amount: float) -> bool:
        """取款"""
        if amount > self.__balance:
            print(f"余额不足！当前余额: ¥{self.__balance:.2f}")
            return False
        elif amount <= 0:
            print("取款金额必须大于0")
            return False
        else:
            self.__balance -= amount
            print(f"取出 ¥{amount:.2f}，余额: ¥{self.__balance:.2f}")
            return True
    
    def get_balance(self) -> float:
        """获取余额"""
        return self.__balance

account = BankAccount("Alice", 1000.0)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)  # 余额不足
print(f"当前余额: ¥{account.get_balance():.2f}")

# 无法直接访问私有属性
# print(account.__balance)  # ❌ 会报错

# ========================================
# 5. 属性装饰器 (@property)
# ========================================
print("\n【5. 属性装饰器】")

class Rectangle:
    """矩形类"""
    
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    
    @property
    def width(self) -> float:
        """宽度属性"""
        return self._width
    
    @width.setter
    def width(self, value: float) -> None:
        """设置宽度"""
        if value <= 0:
            raise ValueError("宽度必须大于0")
        self._width = value
    
    @property
    def height(self) -> float:
        """高度属性"""
        return self._height
    
    @height.setter
    def height(self, value: float) -> None:
        """设置高度"""
        if value <= 0:
            raise ValueError("高度必须大于0")
        self._height = value
    
    @property
    def area(self) -> float:
        """面积 (只读属性)"""
        return self._width * self._height
    
    @property
    def perimeter(self) -> float:
        """周长 (只读属性)"""
        return 2 * (self._width + self._height)

rect = Rectangle(10, 5)
print(f"矩形: 宽={rect.width}, 高={rect.height}")
print(f"面积: {rect.area}")
print(f"周长: {rect.perimeter}")

rect.width = 15  # 使用 setter
print(f"修改后面积: {rect.area}")

# ========================================
# 6. 特殊方法 (Magic Methods)
# ========================================
print("\n【6. 特殊方法】")

class Vector:
    """二维向量"""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        """字符串表示 (用户友好)"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        """官方字符串表示 (开发者友好)"""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other: 'Vector') -> 'Vector':
        """向量加法"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        """向量减法"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: float) -> 'Vector':
        """标量乘法"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other: 'Vector') -> bool:
        """相等比较"""
        return self.x == other.x and self.y == other.y
    
    def __len__(self) -> int:
        """长度 (维度)"""
        return 2
    
    def __getitem__(self, index: int) -> float:
        """索引访问"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("向量索引超出范围")

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1[0] = {v1[0]}, v1[1] = {v1[1]}")

# ========================================
# 7. 类方法和静态方法
# ========================================
print("\n【7. 类方法和静态方法】")

class MathUtils:
    """数学工具类"""
    
    PI = 3.14159
    
    @classmethod
    def circle_area(cls, radius: float) -> float:
        """计算圆面积 (类方法)"""
        return cls.PI * radius ** 2
    
    @staticmethod
    def is_even(number: int) -> bool:
        """判断是否为偶数 (静态方法)"""
        return number % 2 == 0
    
    @staticmethod
    def factorial(n: int) -> int:
        """计算阶乘"""
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)

print(f"圆面积 (r=5): {MathUtils.circle_area(5):.2f}")
print(f"10 是偶数: {MathUtils.is_even(10)}")
print(f"5! = {MathUtils.factorial(5)}")

# ========================================
# 8. 实用案例：购物车系统
# ========================================
print("\n【8. 实用案例：购物车系统】")

class Product:
    """商品类"""
    
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock
    
    def __str__(self) -> str:
        return f"{self.name} (¥{self.price:.2f}) - 库存: {self.stock}"

class ShoppingCart:
    """购物车类"""
    
    def __init__(self):
        self.items = {}  # {product: quantity}
    
    def add_item(self, product: Product, quantity: int = 1) -> None:
        """添加商品"""
        if quantity > product.stock:
            print(f"  ❌ 库存不足！{product.name} 仅剩 {product.stock} 件")
            return
        
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
        
        product.stock -= quantity
        print(f"  ✅ 已添加 {quantity} 件 {product.name}")
    
    def remove_item(self, product: Product) -> None:
        """移除商品"""
        if product in self.items:
            quantity = self.items[product]
            product.stock += quantity
            del self.items[product]
            print(f"  ✅ 已移除 {product.name}")
        else:
            print(f"  ❌ 购物车中没有 {product.name}")
    
    def get_total(self) -> float:
        """计算总价"""
        return sum(product.price * quantity for product, quantity in self.items.items())
    
    def show_cart(self) -> None:
        """显示购物车"""
        if not self.items:
            print("  购物车为空")
            return
        
        print("  购物车内容:")
        for product, quantity in self.items.items():
            print(f"    - {product.name} x{quantity} = ¥{product.price * quantity:.2f}")
        print(f"  总计: ¥{self.get_total():.2f}")

# 使用购物车
laptop = Product("笔记本电脑", 5999.00, 10)
mouse = Product("鼠标", 99.00, 50)
keyboard = Product("键盘", 299.00, 30)

cart = ShoppingCart()
cart.add_item(laptop, 1)
cart.add_item(mouse, 2)
cart.add_item(keyboard, 1)
cart.show_cart()

print("\n" + "=" * 50)
print("✅ 第五课完成！")
print("=" * 50)

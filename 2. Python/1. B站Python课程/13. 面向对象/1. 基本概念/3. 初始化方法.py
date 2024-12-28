# 当使用类名()创建对象时，会自动执行以下操作：
    # 1.为对象在内存中分配空间 --创建对象
    # 2.为对象的属性设置初始值 --初始化方法(init)
    # 这个初始化方法就是__init__方法,__init__是对象的内置方法
    # init方法就是专门用来定义一个类具有哪些属性的方法
class Cat:
    def __init__(self) -> None:
        self.name = "猫猫111"
tom = Cat()
print(tom.name)


# 改进：使用传入的参数对属性进行定义
class Cat2:                             # 定义类不需要括号，使用时需要
    def __init__(self, name) -> None:   # init方法中的传入参数就是使用时括号内传入的参数
        self.name = name
tom2 = Cat2("猫猫222")                  # 传入的参数用于init方法
print(tom2.name)
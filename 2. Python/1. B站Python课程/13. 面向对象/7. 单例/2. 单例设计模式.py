# 单例--让类创建的对象，在系统中只有唯一的一个实例
#   定义一个类属性，初始值是None，用于记录单例对象的引用
#   重写__new__方法
#   如果类属性 is None，调用父类方法分配空间，并在类属性中记录结果
#   返回类属性中记录的对象引用

class ceshi:
    pass
a = ceshi()
b = ceshi()
print(a)    
print(b)    # 返回内存地址不同


# 单例设计模式：
class Demo(object):
    instance = None     # 类初始化时的类属性赋值，第二次创建对象时不会再执行
    def __new__(cls):
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def __init__(self) -> None:
        pass


demo1 = Demo()
demo2 = Demo()
print(demo1)    
print(demo2)    # 两次返回地址相同

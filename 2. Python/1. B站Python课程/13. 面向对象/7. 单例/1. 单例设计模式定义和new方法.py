# 单例设计模式：
#   目的--让类创建的对象，在系统中只有唯一的一个实例
#   每一次执行类名()返回的对象内存地址是相同的


# __new__方法：
# 使用类名创建对象时，python解释器首先会调用__new__方法为对象分配空间
# __new__是由object基类内置的静态方法，主要作用有两个：
#   在内存中为对象分配空间
#   返回对象的引用
# python解释器获得对象的引用后，将引用作为第一个参数，传递给init方法
# 重写__new__方法的代码非常固定！
# 重写new方法的代码非常固定：
#   重写new方法一定要return super().new(cls)
#   否则python解释器得不到分配了空间的对象引用，就不会调用对象的初始化方法
#   注意：new是一个静态方法，调用时需主动传递cls参数


class NewMethodDemo1(object):
    def __new__(cls):
        print("1.1 new方法执行")        

    def __init__(self) -> None:
        print("1.2 init方法执行")       # new方法不返回值初始化方法就不会调用！！
        
demo1 = NewMethodDemo1()
print("1.3", demo1)                     # new方法没有返回值，所以demo对象为空值


class NewMethodDemo2(object):
    def __new__(cls):
        print("2.1 new方法执行")
        instance = super().__new__(cls) # instance用于传递对象    # 注意语法！！
        return instance                 # 有返回对象

    def __init__(self) -> None:
        print("2.2 init方法执行")       # new方法有返回值，所以会执行

demo2 = NewMethodDemo2()
print("2.3", demo2)                     # demo2在内存有地址
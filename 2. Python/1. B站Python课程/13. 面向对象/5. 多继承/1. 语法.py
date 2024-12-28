# 子类可以拥有多个父类，并且具有所有父类的属性和方法
# 只需在类创建时把多个父类用逗号进行分割
class Father1:
    def f1(self):
        print("父类1方法")


class Father2:
    def f2(self):
        print("父类2方法")


class Son(Father1, Father2):    # 啥也不做，只继承两个父类
    pass


son = Son()
son.f1()    # 可以调用父类1
son.f2()    # 可以调用父类2
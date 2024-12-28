# 父类的私有方法和属性不会继承给子类
# 如果子类需要使用父类的私有方法和属性，可以间接通过父类的公有方法使用

class Father:
    def __init__(self) -> None:
        self.num1 = 10
        self.__num2 = 100

    def __ff(self):
        print("私有方法打印：%s%s" % (self.num1, self.__num2))

    def ff(self):
        print("方法打印：%s%s" % (self.num1, self.__num2))      # 在公有方法里面打印私有属性
        self.__ff                                               # 在公有方法里面使用私有方法


class Son(Father):
    pass



ceshi = Son()
ceshi.ff()           # 使用父类的公有方法，父类的私有方法和属性都能间接使用
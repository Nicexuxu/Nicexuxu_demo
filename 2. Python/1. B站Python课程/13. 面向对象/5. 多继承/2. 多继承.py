# 在开发中，如果父类中存在同名的属性或者方法，应该避免使用多继承

class A:                        # AB两个类都有demo1和2两个方法
    def demo1(self):
        print("---Demo1")

    def demo2(self):
        print("---Demo2")


class B:
    def demo1(self):
        print("Demo1")

    def demo2(self):
        print("Demo2")


class Son(A, B):            # Son同时具有AB两个父类
    pass


son = Son()                 
son.demo1()                 # 调用
son.demo2()
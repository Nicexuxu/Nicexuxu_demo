# 局部优先性：子类的直接父类优先于间接父类被查找，也就是子类会优先从离它更近的父类中查找方法
# 以下代码输出结果是 ACBD 而不是 ABD ！！！
class A:
    def method(self):
        print("A's method")
class B(A):
    def method(self):
        super().method()
        print("B's method")
class C(A):
    def method(self):
        super().method()
        print("C's method")
class D(B, C):
    def method(self):
        super().method()
        print("D's method")
d = D()
d.method()
print(D.__mro__)
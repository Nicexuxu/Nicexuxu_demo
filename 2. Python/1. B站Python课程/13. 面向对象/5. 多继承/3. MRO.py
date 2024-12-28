# python针对类提供了一个内置属性__MRO__，可以查看方法搜索顺序
# MRO是（method resolution order）的缩写，用于在多继承时判断方法和属性的调用路径
class A:
    pass
class B:
    pass
class C(A, B):
    pass

print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# 从左向右依次查找，如果找到就执行并停止查找，找不到就继续
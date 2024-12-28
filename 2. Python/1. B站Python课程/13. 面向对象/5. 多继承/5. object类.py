# 新式类与旧式（经典）类：
# object类是python为所有对象提供的基类，提供有一些内置的属性和方法，可以使用dir函数查看
# 
# 新式类：以object为基类的类，推荐使用
# 经典类：不以object为基类的类，不推荐使用
#
# 在python3.x中定义类时，如果没有指定父类，会默认使用object作为基类
# 在python2.x中定义类时，如果没有指定父类，不会以object作为基类
#
# 新式类和经典类在多继承时，会影响到方法的搜索顺序
# 推荐无论python版本，都在父类加上object
class demo:
    pass
d = demo()
print(dir(d))       # 输出demo自带的方法
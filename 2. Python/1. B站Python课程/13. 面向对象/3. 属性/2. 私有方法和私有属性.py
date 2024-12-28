# 私有属性和方法只能在函数内部被使用，在外部使用不了
# 方法或者属性前面加上__可以使其变为私有方法和属性

class Woman:
    def __init__(self) -> None:
        self.__age = "10"

    def __say(self):
        print(self.__age)

a = Woman()
# a.__say()  会报错 


# 在python中没有真正意义上的私有
# 外部使用时，在名称前加上 (_类名) 变成 (_类名_私有属性/方法) 即可访问
# 但是不推荐这么用
a._Woman__say()     # type:ignore
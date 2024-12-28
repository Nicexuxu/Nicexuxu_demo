# 当一个对象从内存中被销毁时，自动调用__del__方法
class Cat:
    def __init__(self) -> None:
        print("初始化方法")
    def __del__ (self):         # 销毁时自动调用
        print("del方法")
    def __str__(self) -> str:
        return "str方法返回的字符串"

tom = Cat()
print(tom)


# 在Python中，使用print输出对象变量，默认会输出这个变量引用的对象是由哪一个类创建的对象，以及在内存中的地址(十六进制表示)
# 如果在开发中，希望使用print输出对象变量时，能够打印自定义的内容，就可以利用str-这个内置方法
# str方法必须返回一个字符串
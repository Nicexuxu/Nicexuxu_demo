# 在开发时，如果一个方法既不需要访问实例属性或者调用实例方法
#                     也不需要访问类属性或者调用类方法
# 就可以将其封装成一个静态方法
# 通过 类名. 调用静态方法

class demo:
    @staticmethod   
    def staticmd():             # 不需要指定第一个参数
        print("静态方法输出")

demo.staticmd()
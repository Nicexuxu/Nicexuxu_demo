# 类方法需要用修饰器@classmethod，告诉解释器这是一个类方法
# 类方法的第一个参数应该是cls（也可用其他的，习惯用cls）
# 通过 类名. 调用类方法时不需要传递cls参数
# 在方法内部可以通过cls.访问类的属性，也可通过cls.调用其他的类方法
class demo:
    leishuxin = "类属性"
    @classmethod
    def ceshi(cls):
        print("类方法输出")         # 在类方法内输出内容
        print(cls.leishuxin)        # 用cls访问类属性

demo.ceshi()
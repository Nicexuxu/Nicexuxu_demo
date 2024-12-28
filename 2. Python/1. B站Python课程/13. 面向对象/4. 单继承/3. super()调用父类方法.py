# 在开发中，如果子类的方法需要对父类进行拓展，而不是简单的继承，
# 可以先重写父类方法
# 在重写的方法内使用 super().父类方法 来调用父类方法的执行
class Father:
    def ff(self):
        print("父类方法")


class Son(Father):
    def ff(self):               # 先直接重写
        print("子类方法")
        super().ff()            # 再用super调用父类方法


ceshi = Son()
ceshi.ff()                      # 最后输出子类ff中的内容，两个都会print出来
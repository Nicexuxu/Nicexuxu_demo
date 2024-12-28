# 在python2.x时用 父类名.方法(self) 来调用
class Father:
    def ff(self):
        print("父类方法")


class Son(Father):
    def ff(self):               # 先直接重写
        print("子类方法")
        Father.ff(self)            # 直接用父类名调用父类方法 # 记得加self


ceshi = Son()
ceshi.ff()                      # 最后输出子类ff中的内容，两个都会print出来
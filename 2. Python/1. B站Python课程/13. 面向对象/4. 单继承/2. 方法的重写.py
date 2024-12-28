# 当父类已有的方法不能满足子类的需求时，可直接重写进行覆盖
class Father:
    def ff(self):
        print("父类的方法")


class Son(Father):
    def ff(self):           # 直接def进行覆盖
        print("子类的方法")

ceshi = Son()
ceshi.ff()                  # 输出子类的方法

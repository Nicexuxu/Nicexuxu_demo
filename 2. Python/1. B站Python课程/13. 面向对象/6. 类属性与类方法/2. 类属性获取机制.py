# 属性获取的向上查找机制：
# 实例名.属性 会先在实例内部查找该属性，如果没找到再到类名找该属性

class ceshi:
    shuxin = "类属性"

a = ceshi()
print(ceshi.shuxin)
print(a.shuxin)     # 二者都会打印出ceshi类的类属性

# 注意：如果使用 对象.类属性=值 的形式，只会给对象添加一个属性，而不会影响到类属性的值
a.shuxin = "实例属性"
print(ceshi.shuxin)
print(a.shuxin)
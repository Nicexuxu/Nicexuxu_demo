# 1. 在形参前加*可以获取多个数值作为元组，加**可以获取字典
def ceshi(can1, *args, **kwargs):     # 只允许一个*和**，且**后不能跟随另外的参数
    print(can1, args, kwargs)

ceshi(1, 2, 3, k="zhi")


# 2. 如果想要传入完整的元组或者字典，可以在传入的变量前加入对应的*(字典和元组的拆包)
def ceshi2(*args, **kwagrs):
    print(args, kwagrs)
list1 = [1, 2]
dict1 = {"1": "2", "3": "4"}
dict2 = {"5": "6", "7": "8"}    # 可以叠加
ceshi2(*list1, **dict1, **dict2)
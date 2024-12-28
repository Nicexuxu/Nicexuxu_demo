# 元组信息查询和列表类似
# 取值
tuple1 = (1, 2, 1, 1)
print(tuple1[1])
# 取索引
print(tuple1.index(1))
# 统计次数
print(tuple1.count(1))
# 取长度值
print(len(tuple1))

# 当元组内只有一个数据的时候,输出会变成里面的内容，而不是一个元组，在那单个内容后面加逗号即可变回元组
print(type(()))
print(type((1)))
print(type((1,)))

# list和tuple函数可以对列表和元组之间进行转换
tuple1 = list(tuple1)
print(tuple1)
tuple1 = tuple(tuple1)
print(tuple1)
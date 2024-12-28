# Python内置函数
a = "2655558"
b = ["a", "as", "s"]


# len用于计算容器中元素个数
print(len(a))

# del用于删除元素，可做函数用，也可做关键字用
del b[0]
print(b)
del(b[0])
print(b)

# max(item)和min(item)用于返回容器中元素和最小值
zifu1 = "awkjhbdkjawbdkjaw"
print(max(zifu1))
print(min(zifu1))
zifu2 = [1, 5, 66, 85, 195, 0.9899656155614]
print(max(zifu2))
print(min(zifu2))
# 如果是字典，只针对key进行比较
zifu3 = {
    "a": 100,
    "b": 22,
    "s": 1
}
print(max(zifu3))
print(min(zifu3))



# 对列表和元组进行切片
print([0, 1, 2, 3, 4, 5, 6][1:3])
print((0, 1, 2, 3, 4, 5, 6)[1:3])
# 字典是无序的，不能进行切片
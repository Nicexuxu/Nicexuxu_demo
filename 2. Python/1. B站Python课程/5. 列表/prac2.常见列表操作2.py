# 1. 统计
list1 = ["内容1", "内容2", "重复", "重复"]
# len(列表名称) len函数可以返回列表的长度
print(len(list1))
# 列表名称.count(数据内容) 可以统计指定数据在列表中出现的次数
print(list1.count("重复"))


# 2. 排序
list2 = ["b", "d", "c", "a"]
list3 = [3, 1, 4, 2]
# 列表名.sort() 可以对列表内容进行升序排序,
list2.sort()
list3.sort()
print(list2)
print(list3)
# 列表名.sort(reverse=True) 可以对列表内容进行降序排序
list2.sort(reverse=True)
list3.sort(reverse=True)
print(list2)
print(list3)
# 列表名.reverse() 可以对列表内容进行翻转
list2.reverse()
list3.reverse()
print(list2)
print(list3)
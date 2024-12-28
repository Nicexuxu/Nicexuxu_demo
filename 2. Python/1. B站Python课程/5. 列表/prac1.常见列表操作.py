# 创建列表
list1 = ["字符1", "字符2"]
list2 = ["列表二内容1", "列表二内容2"]


# 1. 取值和取索引
# 列表名[索引值] 可以输出列表对应值的内容，索引值从零开始
print(list1[1])
# 列表名.index(内容) 可以在知道数据内容的情况下得出数据的位置
print(list1.index("字符1"))
    

# 2. 修改
# 列表名[索引值]=修改的内容 可以修改指定内容
print(list1)
list1[0] = "字符1修改"
print(list1)


# 3. 增加
# 列表名.append 可以向列表的末尾追加数据
list1.append("末尾追加数据")
print(list1)
# 列表名.insert(索引值, 插入的内容) 可以把内容插入到索引值位置，其他内容往后顺延
list1.insert(1, "索引值1插入")
print(list1)
# 列表名.extend(要合并的列表名) 可以把另一个列表插入到已有列表的后面
list1.extend(list2)
print(list1)


# 4. 删除
# 列表名.remove(指定的数据) 可以从列表中删除指定内容的数据，如果数据重复默认删除第一个
list1.remove("字符2")
print(list1)
# 列表名.pop(索引值) 可以删除列表内指定索引值的内容并且返回值，索引值如果不输入默认为删除列表内最后一个值
print(list1.pop(1))
print(list1)
# 列表名.clear() 可以清空列表
list1.clear()
print(list1)
# del 列表名[索引值] del函数也可删除指定数据
print(list2)
del list2[1]
print(list2)
# del本质是从内存中删除一个数据，也可用来删除变量
# del 变量名 可以删除一个变量
del list2
# print(list2) 会报错，print不出来了
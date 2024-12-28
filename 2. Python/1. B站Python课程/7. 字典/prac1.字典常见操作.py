# 键只能使用字符串，数字或者元组，值可以取任何数据类型
dic1 = {"key1": "aa",
        "key2": "bb",}


# 1. 字典的增删改查
# 字典[键] 可以取对应键的值，和列表元组不同，不使用索引值
print(dic1["key2"])
# 字典[键]=值 可以修改对应键的值，如果不存在则创建这个键值对
dic1["key1"] = "修改"
dic1["key5"] = "创建"
print(dic1)
# 字典.pop(键) 可以删除键值对，remove方法在字典中不适用


# 2. 字典的统计，合并，清空操作
# len(字典名) 可以统计键值对数量
print(len(dic1))
# 字典名.update(要合并的字典名) 可以合并字典
# 如果要合并的字典和原有字典键重复，会覆盖原有字典
dic2 = {"keynew": "new"}
dic1.update(dic2)
print(dic1)
# 字典名.clear() 可以清空字典
dic1.clear()
print(dic1)
# 定义一个字典
dic1 = {"Name": "小明",
        "qq": "123456",
        "phone": "10086"}


# 迭代遍历字典
# k是每一次循环中获取到的键值对中的key
for k in dic1:
    print("%s - %s" % (k, dic1[k]))
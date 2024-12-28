str1 = "\t Hello World \n"
str2 = "\t Hello World \n"

# 5. 去除空白字符
# lstrip用于去除左边开头空白字符
# rstrip用于去除右边倒数空白字符
# strip用于删除左右的空白字符,包括转义字符
print(str1)
print(str2)
print(str1.strip())
print(str2.strip())


# 6. 分割和连接字符串
# partition(str) 把字符串分割成一个三元素的元组（str前，str，str后）
# split(str="", num) 以str为分隔符拆分，如果num有指定值，则仅拆分num+1个字符串，str默认包含空格和转义字符
print(str1.split())
# str.join(seq) 以str为分隔符，将seq的所有元素（的字符串表示）合并为一个新的字符串
print("&".join(str1.split()))



# 7. 字符串切片
# 字符串[起始值:末尾值:步长]可以对字符串类型数据进行切片
str = "0123456789"
print(str[0:5:2])
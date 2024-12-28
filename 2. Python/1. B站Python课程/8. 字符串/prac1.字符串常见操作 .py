# 字符串的操作和列表基本类似
str1 = "Hello World Hello World"
isspace = "  \n \t "
istitle = "Hello World Hello World"
StartAndEnd = "StartAndEnd"
find = "helloworld"


# 1. 长度次数位置统计
# len(字符串) 可以统计字符串长度
print(len(str1))
# count方法可以统计一个小字符串出现的次数
print(str1.count("Hello"))
print(str1.count("nocunzai"))
# index方法可以获取某一个指定的字符串出现的位置,字符串里有多个字符按第一个来查找位置，
print(str1.index("llo"))


# 2. 判断
# isspace方法判断是否只含空格和转义字符
print(isspace.isspace())
# istitle方法判断是否标题化（所有单词首字母都是大写）
print(istitle.istitle())

# isalnum 字符串至少有一个字符并且所有字符都是字母或数字返回True
# isalpha 字符串至少有一个字符并且所有字符都是字母则返回True

# isdecimal 字符串只包含数字则返回True 全角数字
# isdigit   字符串只包含数字则返回True 全角数字 (1) \u00b2
# isnumeric 字符串只包含数字则返回True 全角数字 汉字数字

# islower 如果字符串包含至少一个区分大小写的字符，并且所有这些（区分大小写的）字符都是小写则返回True
# isupper 如果字符串包含至少一个区分大小写的字符，并且所有这些（区分大小写的）字符都是大写则返回True


# 3. 查找和替换
# startswith方法用于判断是否以指定的字符串开始
# endswith方法用于判断是否以指定的字符串结束
print(StartAndEnd.startswith("Start"))
print(StartAndEnd.endswith("End"))
# find方法用于查找指定字符串
# 如果find方法找不到指定字符串，会返回-1
# 如果index方法找不到指定字符串，会报错
print(find.find("hello"))
print(find.find("hillo"))
# replace方法用于替换字符串
# replace方法执行后会返回值，但是原字符串并不会被修改
print(find.replace("hello", "Hello"))
print(find)


# 4. 文本对齐
# ljust(chang) 返回一个字符串左对齐，并用空格填充至长度chang的新字符串
# rjust(chang) 返回一个字符串右对齐，并用空格填充至长度chang的新字符串
# ljust(chang) 返回一个字符串居中，并用空格填充至长度chang的新字符串
print(find.ljust(20))
print(find.rjust(20))
for i in "Hello World":
    print("|%s|" % i.center(5, "-"))
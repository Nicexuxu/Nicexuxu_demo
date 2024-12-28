# eval()函数可以将字符串当成有效的表达式来求值并返回计算结果
# 基本的数学计算
print(eval("1 + 1"))
# 字符串重复
print(eval("'*' * 10"))
# 将字符串转换成列表
print(type(eval("[1, 2, 3]")))
# 将字符串转换成字典
print(type(eval('{"a": "a", "b": "b", "c": "c"}')))

# 注意：千万不要直接转换input的内容
eval(input("请输入算术题："))
# __import__('os').system('dir')
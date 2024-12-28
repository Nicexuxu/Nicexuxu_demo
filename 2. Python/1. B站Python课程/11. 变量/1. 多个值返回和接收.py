# 1. 函数如果有多个返回值可以用元组返回
def c1():
    a = 1
    b = 2
    return (a, b)
print(c1())

# 2. 函数返回多个值可省略元组括号，可用多个变量接收
def c2():
    c = 1
    d = 2
    return c, d
jieshou1, jieshou2 = c2()
print(jieshou1, jieshou2)


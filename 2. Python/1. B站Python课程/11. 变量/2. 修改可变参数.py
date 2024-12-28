# 1. 在函数内对传入参数进行赋值，不会影响原参数的值
#    在函数内对传入的可变参数使用方法进行修改，会全局改变该参数的值

def ceshi(canshu):
    print(canshu)           # 修改前
    canshu.append(123)      # 使用方法进行修改

biaoge = [1, 2, 3]
ceshi(biaoge)
print(biaoge)               # 函数无返回值，但是变量却改变了



# 2. 对列表变量进行+=赋值其实就是调用了extend方法

def ceshi2(canshu2):
    print(canshu2)
    canshu2 += ["+"]
    print(canshu2)

biaoge2 = [1, 2, 3]
ceshi2(biaoge2)
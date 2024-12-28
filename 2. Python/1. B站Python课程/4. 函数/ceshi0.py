def buqiantao():
    print("不嵌套")


a = 1
while a < 10:
    print("输出%d" % a)
    a += 1
    if a == 9:
        def qiantao():
            print("嵌套测试")

#结论：import py文件后会先将文件执行一遍，有执行过def函数才会定义
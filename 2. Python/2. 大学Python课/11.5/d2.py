# 初始变量命名
time = 0
mark = 0
markall = 0
list1 = []


# 逻辑部分
# 一层循环用于输入成绩
while True:
    
    # 输入成绩并记录
    mark = float(input("请输入成绩"))
    list1.append(mark)
    time += 1
    
    #二层循环用于判断是否继续
    while True:
        con = input("回答yes继续输入成绩，回答no停止输入并计算")
        # 如果no就退出二层循环      为c赋True便于一层循环判断是否继续循环
        if con == "no":
            c = True
            break
        # 如果不规范输入，不退出二层循环，在循环内重新输入
        elif con != "yes":
            print("规范输入")
        # 回答yes也退出二层循环     为c赋False便于一层循环判断是否继续循环
        else:
            c = False
            break
    
    #判断是否再输入成绩
    if c:
        break
    else:
        continue


#最后计算输出
for i in list1:
    markall += i
print(markall/time)
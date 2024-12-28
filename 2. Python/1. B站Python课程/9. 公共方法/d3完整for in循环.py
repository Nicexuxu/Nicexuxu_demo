list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 定义列表内容
list2 = range(10000)
xz = int(input())                       # 用户输入寻找的数


for i in list2:                          # 遍历表格寻找
    
    if i == xz:
        print("找到了：", xz, sep="")
        break                           # 找到后break
    else: print("不是", i,sep="")

else: print("已经寻找完，没有找到")       # 遍历完没找到才print
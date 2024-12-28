# 1. 函数参数传入时，在形参后面加上=可以指定缺省参数，即不输入时默认的值
def ceshi(can1, can2="没输入"):
    print(can1, end="")
    print(can2)
ceshi(1)
ceshi(1, "2")



# 2. 参数传入时，缺省参数应该在后面
def ceshi2(can1, can2="", can3=""):    # (can1, can2="", can3)会报错
    print()


# 3. 参数传入时可以指定要传入的参数
def ceshi3(can1, can2="moren2", can3=""):
    print(can1, can2, can3)
ceshi3("这是can1的内容", can3="指定can3")
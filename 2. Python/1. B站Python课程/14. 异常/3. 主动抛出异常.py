# 在python中，除了代码执行出错python会抛出异常意外，
# 还可以根据应用程序特有的业务需求主动抛出(raise)异常

# 需求：
#   定义input_password函数，提示用户输入密码
#   如果密码长度<8，抛出异常
#   如果密码长度>=8，返回输入的密码

def input_password():
    err = Exception("长度错误")     # 手动创建错误类
    pswd = input("请输入密码：")
    if len(pswd) < 8:
        raise err                   # 如果长度小于8，抛出自己添加的err错误
    else:
        return pswd                 # 其他情况返回输入的密码
    
try:
    print(input_password())
except Exception as pr:             # 收集未知错误
    print("出错了", pr)              # 打印出来

ces = Exception()
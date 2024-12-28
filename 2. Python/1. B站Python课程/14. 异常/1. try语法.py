'''
try:
    尝试执行的代码
except 错误类型1:
    针对错误类型1对应的代码处理
except (错误类型2, 错误类型3):
    针对错误类型2和3针对的处理
except Exception as 变量名:
    针对其他错误的处理（把其他错误作为变量传入）
else:
    没有异常才会执行的代码
finally:
    无论是否异常最后再执行的代码
'''

try:
    a = int(input("请输入整数："))
    aa = 8/a
    print(aa)
except ValueError:
    print("请输入整数")
except ZeroDivisionError:
    print("不要输入0")
except Exception as exc:
    print("计算失败：%s" % exc)
else:
    print("成功计算")
finally:
    print("程序结束")
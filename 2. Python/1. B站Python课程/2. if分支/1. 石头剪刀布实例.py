import random as r

player = 0

while not (
        (player == 1)
        or(player == 2)
        or(player == 3)
):
    player = int(input("请输入你要出的手势，石头（1），剪刀（2），布（3）："))
    computer = r.randint(1, 3)
    if not (
        (player == 1)
        or(player == 2)
        or(player == 3)
):
        print("请在规定范围内输入")

print("你给的是%d,电脑给的是%d" % (player, computer))

if (                                        #犯过的错：
    (player == 1 and computer == 2)         #1. #输入成&，找了好久的错误
    or (player == 2 and computer == 3)      #2. 一开始对同一括号换行逻辑不太了解，等于判断==写成赋值=
    or (player == 3 and computer == 1)      #3. if列下括号内and写成了逗号，导致逻辑出错，括号内容变成元组，非空元组总是为True，所以总是输出win
):
    print("win啦！")
elif player == computer:
    print("哦吼，平局！")
else:
    print("废物，这都能输")

input()

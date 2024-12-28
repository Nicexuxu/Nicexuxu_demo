list1 = []
name = ("黑桃", "红桃", "梅花", "方块")
shunxu = ("3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2")
for i in shunxu:
    for j in name:
        tuple1 = (j, i)
        list1.append(tuple1)
print(list1)
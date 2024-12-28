import random

time = 0

r = random.randint(1,200)
print("r是%d" % r)

while r < 201:
    r = random.randint(1,200)
    if r == 2:
        continue
    print("while循环内", r)
    time += 1
print(time)
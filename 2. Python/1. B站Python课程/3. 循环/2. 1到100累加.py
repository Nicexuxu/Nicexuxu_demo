time = 0
result = 0

while time < 101:
    if time%2 == 0:
        result += time

    time += 1
print(result)
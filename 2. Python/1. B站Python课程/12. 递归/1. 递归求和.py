def sum_numbers(num):
    if num == 1:
        return num
    sum = sum_numbers(num-1)
    return sum + num

print(sum_numbers(int(input(""))))
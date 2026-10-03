def digits(num):
    #num = 1542
    count = 0
    while num > 0:
        num = num // 10
        count = count + 1
    return count

print(digits(24524))
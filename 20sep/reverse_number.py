#using while loop
def reverse(num):
    #num = 523
    reversed_num = 0
    while(num > 0):
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num

if __name__ == "__main__":
    print(reverse(123))

# string slicing
# digits = "123456789"
# print(digits[0:6:2])

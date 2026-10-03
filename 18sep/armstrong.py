def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    # n = 45 --> digits = "45" --> power = len("45") = 2
    # If 4^2 + 5^2 = 45, then 45 is armstrong number
    return sum(int(d) ** power for d in digits) == n

def count_armstrong_numbers(start, end):
    count = 0

    for i in range(start, end + 1):
        if is_armstrong(i):
            count += 1

    return count

num = int(input())
if is_armstrong(num):
    print(num, "is armstrong number")
else:
    print(num ,"is not armstrong number")


start = int(input())
end = int(input())
# armstrong_nums = list(filter(is_armstrong,range(start, end +1)))
armstrong_nums = [i for i in range(start, end+1) if is_armstrong(i)]
print(f"The armstrong numbers between {start} and {end}:{armstrong_nums}")

# digits = "45"
# for d in digits:
#     print(type(d))
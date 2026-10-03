# def count_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count+=1
#
# counter = list(count_to(4))
# print(counter)

num = 10
counter = (count for count in range(1, num+1))

for n in counter:
    print(n)

file_path = "C:/Users/user/Desktop/hp.txt"
with open(file_path, 'r') as file:
    lines = (line for line in file)
    for line in lines:
        print(line)
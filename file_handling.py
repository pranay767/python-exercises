file1 = open("end.txt",'r')
file1.seek(1)
lines = file1.read()
print(lines)
# words = lines.split()
# count = words.count('Pranay')
# print(count)

file1.seek(0)

count = 0
for line in file1:
    count += 1
    print(line)
print("Number of lines:", count)
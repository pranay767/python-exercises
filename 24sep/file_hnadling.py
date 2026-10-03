'''
open
read, wwrite
close

Modes:
r - read
w - write
a - append
r+ - read and write
'''

# file1 = open("start.txt",mode='r+')
# file_content = file1.read()
# print(file_content)
# file1.write("pinochio")
# file1.seek(0)
# print(file1.read())
# file1.close()]


# file1 = open("start.txt",mode='r')
#
# print(file1.read())

# file1 = open("start.txt",'w')
# file1.write("pinocchio is lying")
# file1.write("\npinocchio is lying")

file1 = open("end.txt",'r')
print(file1.readline())
#points to the
print(file1.readline())
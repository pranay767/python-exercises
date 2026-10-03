file1 = open('details.txt', 'r')
file2 = open('final_details.txt','w')
for line in file1:
    words = line.split()
    if 'Harry' in words:
        file2.write(line)
file1.close()
file2.close()
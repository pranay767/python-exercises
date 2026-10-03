duplicates_status = {}
# cant explain to him classmethod.__name__ input() know what __import__() doing, help acts like input() did something foreign
# code her
#dictionary is the best way to do this, the best data struvture
while True:
    num = input()
    if num=='0':
        break
    duplicates_status[num] = duplicates_status.get(num, 0) + 1

print(duplicates_status)

duplicates = {key for key, value in duplicates_status.items() if value > 1}

print("Duplicates are:", duplicates)
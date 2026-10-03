para = "The tomb is is definitely haunted haunted"
words = para.split()
print("No of words:", len(words))

uniqueness = dict()
for word in words:
    if word in uniqueness:
        uniqueness[word] += 1
    else:
        uniqueness[word] = 1

unique_values = sum(1 for value in uniqueness.values() if value == 1)

print("No of unique words:", unique_values)
most_frequent_word = key for max(uniqueness.values())

# [the, tomb, is, haunted, the , tomb, tomb, the ,is , an]
# ---> set
# {the, tomb, is , haunted, an}
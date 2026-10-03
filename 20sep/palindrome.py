from reverse_number import reverse

#for numbers
def is_palindrome(num):
    if num == reverse(num):
        return True
    else:
        return False

# for strings
def is_palindrome_word(word):
    return word == word[::-1]

print(is_palindrome(2332))
print(is_palindrome_word("traart"))

'''
word = "mystery series"
print(word[11:2:-2])
print(word[::2])#print(word[0:14:2])
#so word[::+] --> word[0:14:+]
# and word[::-] --> word[13:-1:-]
print(word[::-2])#print(word[13:-1:-2])
print(word[::-2])
# negative opposite direction..the - indicates we move backward'''
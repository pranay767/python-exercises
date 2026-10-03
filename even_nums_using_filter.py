import random

# def is_even(n):
#     n%2==0:
#         return True
#     return False

nums = [random.randint(1,100) for i in range(10)] #list comprehension
print("Numbers list:", nums)
even_nums = list(filter(lambda n : n % 2==0,nums))
doubles = list(map(lambda n:n*2,even_nums))
print("Even numbers:", even_nums)
print("Doubled evens numbers:", doubles)


#the changes m,ade between the last commit and the current one. Thats what is stored in the new commit,
# what all changes were amde .. comparing both
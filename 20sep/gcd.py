def gcd(num1, num2): #recursive function
    num1, num2 = max(num1, num2), min(num1,num2) # num1 = 48 ,num2 = 14
    while num2 > 0: #num1 % num2 = 6
        return gcd(num2,num1 % num2)
    return num1

print(gcd(14,48))

'''
gcd(48,14) = gcd(14,6)
           = gcd(6,2)
           = 2

56 : 1,2,4,7,8,14,28,56

given a number can i already know hpw many divisors itll have?
say 56 ---. it has 8 divisors.. does the latter have anything to do with the former?
almost square root right....

12: 1 2 3 4 6 12 ---> 12 has 6 divisors
20: 1 2 4 5 10 20 ---> 20 has 6 divisors
26: 1 2 13 26 ---> 26 has 4 divisors
22
80
'''
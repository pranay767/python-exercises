def is_prime(n):
    #1 --- n will anyone devide n comepletyle, besides 1 and n
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

print(is_prime(8))
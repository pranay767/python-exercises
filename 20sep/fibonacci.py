def fibonacci(limit):
    fibonacci_sequence = []
    a,b = 0,1
    for i in range(limit):
        fibonacci_sequence.append(a)
        a,b= b, a+b
    return fibonacci_sequence

print(fibonacci(10))
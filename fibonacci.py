def fibonacci(n):
    if n < 0:
        raise Exception("Enter valid input")
    
    elif n == 0 or n == 1:
        return n
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i

    return fact

print("Hello World")

#recursion
def factorial(n):
    if n == 0 or n == 1: return 1
    else: return factorial(n-1)
    
#fibonacci version of recursion
def fibonacci(n):
    if n == 1: return 0
    elif n == 2: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)

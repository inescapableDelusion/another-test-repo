print("Hello World")

#recursion
#this is to be repeated again and again and again.
def factorial(n):
    if n == 0 or n == 1: return 1
    else: return factorial(n-1)
    
#fibonacci version of recursion
def fibonacci(n):
    if n == 1: return 0
    elif n == 2: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)

#let us test our recursion functions
#this is a test in order to stop the [sample] issue
print("The factorial of 6 is {}.".format(factorial(6))
print("The 15th fibonacci term is {}.".format(fibonacci(15))
      
#this is just for the sample lol
#anytime now? lol
#I am editing this, again...


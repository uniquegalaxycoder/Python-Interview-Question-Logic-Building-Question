#  Calculate and print the factorial of a given number.

        # Using While Loop
num = 5
start = 1 
factorial = 1 

while start <= num :
    factorial = factorial * start
    start += 1 
print(factorial)

        # Using Recursion methods
def factorial(n):
    if n == 0 :
        return 1 
    return n * factorial(n-1)
    
print(factorial(5))

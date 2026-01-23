"""
    Q.Print the Fibonacci series up to n terms.
"""

num = 10 
i = 0 
a = 0 
b = 1

while i < num :
    print(a, end=" ")
    c = a + b 
    a = b 
    b = c
    i += 1

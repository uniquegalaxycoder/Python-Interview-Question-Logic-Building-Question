"""
    Print all factors of the given number. 
"""

num = 110
i = 1 
while i < num :
    if num % i == 0 :
        print(i, end=" ")
    i += 1 

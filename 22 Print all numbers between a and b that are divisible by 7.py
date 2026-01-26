"""
  Print all numbers between a and b that are divisible by 7.
"""

a = 1 
b = 50 

while a < (b+1) :
    if a % 7 == 0 :
        print(a, end=" ")
    a += 1

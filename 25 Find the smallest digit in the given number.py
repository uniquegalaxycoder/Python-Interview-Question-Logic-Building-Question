"""
  Find the smallest digit in the given number. 
"""

num = 5123

i = 0 
small_num = float("inf")

while num > 0 :
    digit = num % 10 
    if digit < small_num :
        small_num = digit 
    num = num // 10
    
print(small_num)

"""
  Find the largest digit in the given number. 
"""

num = 5123 
large_num = float("-inf")

while num > 0 :
    digit = num % 10 
    if digit > large_num :
        large_num = digit 
    num = num // 10
    
print(large_num)

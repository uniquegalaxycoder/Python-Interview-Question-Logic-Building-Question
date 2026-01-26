"""
  Find and print the sum of all factors of the given number.
"""

num = 20 
i = 1
sums = 0 
while i < num :
    if num % i == 0 :
        sums += i
        print(i)
    i += 1 
    
print(f"sum : {sums}")

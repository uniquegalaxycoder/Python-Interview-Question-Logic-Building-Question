"""
  Q.Check whether the given number is a Perfect number. 

NOTE  :    A perfect number is a positive integer that equals the sum of its proper positive divisors (all divisors except the number itself).
          For example, 6 is a perfect number because its proper divisors are 1, 2, and 3, and 1 + 2 + 3 = 6. The next perfect numbers are 28, 496, and 8128,
          known since antiquity.
"""

num = 6

temp_num = num -1  
#here num -1 all divisors except the “number itself”

sums = 0 

while temp_num > 0 :
    if num % temp_num == 0 :
        sums += temp_num
    temp_num -= 1

if num == sums :
    print(f"{num} is a perfect number")
else :
    print(f"{num} is not a perfect number")

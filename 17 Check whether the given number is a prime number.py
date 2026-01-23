"""
  Q.Check whether the given number is a prime number. 
    NOTE :  Prime number is only divisible by 1 or itself.
"""

num = -7 
temp_num = num -1 

if num > 0 :
    while temp_num > 1 :
        if num % temp_num == 0 :
            print("Not prime")
            break 
        temp_num -= 1 
    else :
        print("Prime")
else :
    print("Check number, input positive number")

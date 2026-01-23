# Find and print the sum of digits of the given number. 

user_value = 123455
num = user_value  
# created a copy of original number

sums = 0 

while num > 0 :
    digit = num % 10 
    sums += digit 
    num = num // 10

print(sums)

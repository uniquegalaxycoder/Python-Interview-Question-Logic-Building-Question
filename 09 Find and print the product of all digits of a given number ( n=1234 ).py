# Find and print the product of all digits of a given number ( n=1234 ). 

num = 1234
product = 1

while num > 0 :
    digit = num % 10 
    product = product * digit
    num = num // 10
    
print(product)

# Find and print the product of all digits of a given number ( n=12345 ). 

num = 12345
product = 1

while num > 0 :
    digit = num % 10 
    
    product = product * digit
    print(digit, end=" ")
    num = num // 10
    
print(f"Product : {product} ")

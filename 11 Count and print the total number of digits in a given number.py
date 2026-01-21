"""
  Q.Count and print the total number of digits in a given number. 
"""

num = 12345

count = 0 

while num > 0 :
    digit = num % 10 
    count += 1 
    print(digit, end = " ")
    num = num // 10

print(f"\nTotal Digit : {count}")

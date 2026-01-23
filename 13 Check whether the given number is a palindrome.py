# Check whether the given number is a palindrome. 

original_num = 1212              
# used to keep as it is original value

num = original_num               
# used new variable for copy of original  value

reverse_num = 0 

while num > 0 :
    digit = num % 10 
    reverse_num = reverse_num * 10 + digit
    num = num // 10
    
if num == reverse_num :
    print(f"{original_num} is palindrome")
else :
    print(f"{original_num} is not a palindrome")

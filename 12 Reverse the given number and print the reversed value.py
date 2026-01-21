"""
    Q.Reverse the given number and print the reversed value. 
"""

nums = 9876

reverse_num = 0 

while nums > 0 :
    digit = nums % 10
    reverse_num = reverse_num * 10 + digit 
    nums = nums // 10
    
print(f"Reversed Number : {reverse_num}")

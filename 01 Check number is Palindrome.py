"""
    Q.Check number is Palindrome
"""

def numPalindrome(num:int) -> str:
    new_num = num 
    
    reverse_num = 0
    
    while new_num > 0 :
        digit = new_num % 10 
        reverse_num = reverse_num * 10 + digit 
        new_num = new_num // 10
    
    if num == reverse_num :
        return f"{num} is palindrome"
    else :
        return f"{num} is not palindrome"
        
num = 321 
print(numPalindrome(num))

"""
Time Complexity -> O(n)
Space Complexity -> O(1)

"""

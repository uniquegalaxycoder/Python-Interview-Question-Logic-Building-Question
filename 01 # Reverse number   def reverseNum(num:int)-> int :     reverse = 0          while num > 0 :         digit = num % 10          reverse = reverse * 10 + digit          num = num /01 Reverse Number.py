""" Reverse number  """

def reverseNum(num:int)-> int :
    reverse = 0
    
    while num > 0 :
        digit = num % 10 
        reverse = reverse * 10 + digit 
        num = num // 10
        
    return f"Reverse Number : {reverse} "

num = 123
print(reverseNum(num))

"""
  Space Complexity -> O(1)
  Time Complexity -> O(n)
"""

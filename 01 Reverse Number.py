"""
    Q.Preverse Number
"""

def ReverseNumber( num:int )-> int :
  reverse_num = 0 

  while num > 0 :
    digit = num % 10 
    reverse_num = reverse_num * 10 + digit
    num = num // 10 
  return reverse_num 

num = 121
print(ReverseNumber(num))

"""
Time Complexity -> O(n)
Space Complexity -> O(1)
"""

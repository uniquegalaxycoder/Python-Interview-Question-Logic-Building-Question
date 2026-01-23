# Check whether the given number is an Armstrong number.
 Note : An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

main_num = 153

temp_num = main_num
# created a copy of original number

n = len(str(temp_num))
sums = 0 

while temp_num > 0 :
    digit = temp_num % 10
    sums += digit ** n 
    temp_num = temp_num // 10 
    
if main_num == sums :
    print(f"{main_num} Number is Armstrong")
else :
    print(f"{main_num} Number is not Armstrong")

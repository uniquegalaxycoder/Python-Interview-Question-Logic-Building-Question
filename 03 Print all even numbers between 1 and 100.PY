# Print all even numbers between 1 and 100. 
 
# Using bitwise '&' operator 
start = 1 
end = 100

while start <= end :
    if (start & 1) == 0 :
        print(start, end=" ")
    start += 1 
     
# Using remainder 0 
start = 1 
end = 100 

while start <= end :
    if start % 2 == 0 :
        print(start, end=" ")
    start += 1 


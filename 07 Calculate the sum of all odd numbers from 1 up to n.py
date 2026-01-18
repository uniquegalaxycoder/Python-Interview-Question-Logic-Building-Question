# Calculate the sum of all odd numbers from 1 up to n. 

start = 1 
end = 10
odd_sum = 0 
while start <= end :
    if (start & 1) != 0 :
        odd_sum += start 
    start += 1 
    
print(odd_sum)

# . Calculate the sum of all even numbers from 1 up to n. 

start = 1 
end = 10
sums = 0
while start < end+1 :
    if start % 2 == 0 :
        sums += start
    start += 1
print(sums)

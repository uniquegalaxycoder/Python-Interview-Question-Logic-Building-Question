"""
    Q.Print all prime numbers between 1 and 100.
"""

start = 1 
end = 100 

while start <= end :
    if start % 2 != 0 :
        print(start, end=" ")
    start += 1

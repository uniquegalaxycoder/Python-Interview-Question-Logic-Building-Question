#  Print the multiplication table of a given number from n × 1 to n × 10. 

start = 1 
end = 10 
num = 3

while start <= end :
    numbers = num * start 
    print(f " {num} x {start} = {numbers} " )
    start += 1 

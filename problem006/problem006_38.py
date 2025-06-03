import math
n = int(input())

if n==0:
    a=100000
    
else:
    c = int(100)
    for i in range(n):
        num = c*1.05
        c = math.ceil(num)
        a = c*1000
        
print(a)

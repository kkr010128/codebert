import math

n=int(input())
a=100000

for i in range(n):
    a=a+a*0.05
    if a%1000==0:
        a=a
    else: 
        a=(math.floor(a/1000))
        a=a*1000+1000

print(a)

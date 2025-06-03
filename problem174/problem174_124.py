from math import *
s=0
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            g=gcd(i,j)
            g=gcd(g,k)
            s+=g
print(s)

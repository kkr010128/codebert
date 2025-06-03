n = int(input())
import math
l=0
for i in range(1,n+1):
    for j in range(1,n+1):
        p=math.gcd(i,j)
        for k in range(1,n+1):
            l+=math.gcd(p,k)
print(l)
            

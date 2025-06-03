K=int(input())
import math
l=[]
for i in range(1,K+1):
    for j in range(1,K+1):
        for k in range(1,K+1):
            x=math.gcd(i,math.gcd(j,k))
            l.append(x)
print(sum(l))
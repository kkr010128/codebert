# ABC150 D
from math import gcd

N,M=map(int,input().split())
A=list(map(int,input().split()))

g=A[0]
check=g&-g
for a in A:
    if check!=a&-a:
        check=-1
        break
    g=g*a//gcd(a,g)
if check>=0:
    g//=2
    print((M//g+1)//2)
else:
    print(0)
N,M=map(int, input().split())
from collections import defaultdict
A=list(map(int, input().split()))
B=[]
import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)
# a 偶数
twos=0
D=defaultdict(int)
for i in range(N):
    B.append(A[i]//2)
    a=A[i]
    now=0
    while a%2==0:
        a//=2
        now+=1
    D[now]+=1
    twos=max(twos, now)
if len(set(D.values()))!=1:
    print(0)
    exit()
now=1
for i in range(N):
    now=lcm(now, B[i])

# 1.5 * 3 2*5
from math import ceil
ans=M//(now*pow(2,twos))+1
#res=now+now%(2**twos)
ans=ceil(M//now/2)
#if M-res>0:
#    ans-=int((M-res)//now/(2**twos))

print(ans)
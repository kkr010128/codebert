n,m=map(int,input().split())
h=list(map(int,input().split()))
AB=[list(map(int,input().split())) for _ in range(m)]
from math import gcd
ans=[1 for _ in range(n)]

for ab in AB:
    if h[ab[0]-1]>h[ab[1]-1]:
        ans[ab[1]-1]=0
    elif h[ab[0]-1]<h[ab[1]-1]:
        ans[ab[0]-1]=0
    else:
        ans[ab[0]-1]=0
        ans[ab[1]-1]=0


print(sum(ans))
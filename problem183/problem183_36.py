import sys
input = sys.stdin.readline
from collections import *

def make_divs(n):
    divs = []
    i = 1
    
    while i*i<=n:
        if n%i==0:
            divs.append(i)
            
            if i!=n//i:
                divs.append(n//i)
        
        i += 1
    
    return divs

N = int(input())
ds = make_divs(N)
ans = 0

for d in ds:
    if d==1:
        continue
    
    N2 = N
    
    while N2%d==0:
        N2 //= d
    
    if (N2-1)%d==0:
        ans += 1
    
ans += len(make_divs(N-1))-1
print(ans)
from collections import Counter
from math import gcd

N=int(input())

def factorize(x):
    i=2
    ret=[]

    while i*i<=x:
        while x%i==0:
            ret.append(i)
            x//=i
        
        i+=1
    
    if x>1:
        ret.append(x)
    
    return Counter(ret)

ans=1

for v in factorize(N-1).values():
    ans*=v+1

ans-=1

cnt=1
for v in factorize(gcd(N,N-1)).values():
    cnt*=v+1
cnt-=1

ans-=cnt

k=2
while k*k<=N:
    if N%k==0:
        n=N//k
        while n%k==0:
            n//=k
        
        if n%k==1:
            ans+=1
    k+=1
ans+=1

print(ans)
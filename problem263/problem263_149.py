# ABC 147 D

N=int(input())
A=list(map(int,input().split()))
res=0
p=10**9+7

bits=[0]*71
for a in A:
    j=0
    while a>>j:
        if (a>>j)&1:
            bits[j]+=1
        j+=1

t=0
n=70
while n>=0:
    if bits[n]!=0:
        break
    n-=1

for a in A:
    j=0
    while j<=n:
        if (a>>j)&1:
            res+=((2**j)*(N-bits[j]))%p
        else:
            res+=((2**j)*bits[j])%p
        j+=1
    t=res
print((res*500000004)%p)
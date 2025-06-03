#E
from math import gcd
N=int(input())
A=list(map(int,input().split()))
GCD=A[0]
for i in range(1,N):
    GCD=gcd(GCD,A[i])
    
def Fast_PFact(n):
    List=[0 for i in range(n+1)]
    List[1]=1
    for i in range(2,n+1):
        if List[i]==0:
            cnt=1
            while i*cnt<=n:
                List[i*cnt]=i
                cnt+=1
    return List

if GCD==1:
    P=Fast_PFact(10**6)
    L=[False for i in range(10**6+1)]
    flag=False
    for i in range(N):
        a=A[i]
        while a>1:
            if L[P[a]]:
                flag=True
                break
                
            else:
                L[P[a]]=True
                divisor=P[a]
                while divisor==P[a]:
                    a=int(a/divisor)        
    if flag:
        ans="setwise coprime"
    else:
        ans="pairwise coprime"
else:
    ans="not coprime"
print(ans)
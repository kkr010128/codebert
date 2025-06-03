N=int(input())
*A,=map(int,input().split())
M=max(A)
B=[1]*(M+1)
B[0]=B[1]=1
i=2
while i<=M:
    if B[i]:
        j=2
        while i*j<=M:
            B[i*j]=0
            j+=1
    i+=1

C=[0]*(M+1)
for a in A:
    C[a]=1

from math import*
now=A[0]
for a in A:
    now=gcd(now,a)
if now==1:
    ans='pairwise coprime'
    i=2
    while i<=M:
        if B[i]:
            count=0
            j=1
            while i*j<=M:
                count+=C[i*j]
                j+=1
            if count>1:
                ans='setwise coprime' 
        i+=1
    print(ans)
else:
    print('not coprime')
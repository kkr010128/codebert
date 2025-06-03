def power(a,n):
    x=1
    L=list(format(n,'b'))
    l=len(L)
    for i in range(l):
        if int(L[l-i-1])==1:        
            x=(x*a)%(10**9+7)
        a=(a*a)%(10**9+7)
    return x
N,K=map(int,input().split())
A=list(map(int,input().split()))
b=sorted(A)
c=sorted(A,reverse=True)
D=[]
M=0
x=1
y=1
for l in range(K-1):
    x=(x*(N-l-1))%(10**9+7)
    y=(y*(l+1))%(10**9+7)
y=power(y,10**9+5)
M+=(x*y*(c[0]-b[0]))%(10**9+7)
for i in range(1,N-K+1):
    y1=power(N-i,10**9+5)
    x=(x*y1)%(10**9+7)
    x=(x*(N-K-i+1))%(10**9+7)  
    m=(x*y*(c[i]-b[i]))
    if m>0:
        m=m%(10**9+7)
    M+=m
    M%(10**9+7)

print(M%(10**9+7))






N,K=map(int,input().split())
P=list(map(int,input().split()))
L=[]
M=[0]
c=0
m=0
x=0
for i in range(200100):
    c+=i
    L.append(c)
for i in P:
    m+=L[i]/i
    M.append(m)
if N!=K:
    for i in range(N-K+1):
        x=max(M[K+i]-M[i],x)
else:
    x=M[K]-M[0]
print(x)
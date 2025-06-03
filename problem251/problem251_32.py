f=lambda:map(int,input().split())
N,K=f()
r,s,p=f()
T=list(input())
F=[0]*N
res=0
for i in range(N):
    if F[i]==1:
        continue
    if i+K<N:
        if T[i]==T[i+K]:
            F[i+K]=1
    if T[i]=='s':
        res+=r
    elif T[i]=='p':
        res+=s
    else:
        res+=p
print(res)
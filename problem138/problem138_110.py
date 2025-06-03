N,S=map(int,input().split())
A=list(map(int,input().split()))
pr=998244353
def gya(n):
    return pow(n,pr-2,pr)
p=pow(2,N-1,pr)
l=[0]*(S+1)
g=gya(2)
for i in A:
    for j in range(S-i,-1,-1):
        l[i+j]=(l[i+j]+(l[j]*g))%pr
    if i<=S:
        l[i]+=p
print(l[-1])
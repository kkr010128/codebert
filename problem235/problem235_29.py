N=int(input())
*A,=map(int, input().split())
M=10**3

P=[]
isp=[True]*M
for n in range(2,M):
    if isp[n]==False: continue
    P.append(n)
    for m in range(n*n, M, n):
        isp[m]=False

from collections import defaultdict
D=[defaultdict(int) for _ in range(N)]
for i in range(N):
    a=A[i]
    for p in P:
        while a>1:
            if a%p==0:
                D[i][p]+=1
                a//=p
            else:
                break
        else:
            break
    if a>1:
        D[i][a]+=1

d=defaultdict(int)
for i in range(N):
    for k,v in D[i].items():
        d[k] = max(d[k], v)
gcd=1
for k,v in d.items():
    gcd*=k**v

print(sum([gcd//a for a in A])%(10**9+7))

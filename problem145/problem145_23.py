import sys
N,M=map(int,input().split())
adj={}
for ln in sys.stdin:
    A,B=map(int,ln.split())
    if A not in adj: adj[A]=[]
    if B not in adj: adj[B]=[]
    adj[A].append(B)
    adj[B].append(A)

a=[0]*(N+1)
a[1]=-1
que=[1]
while que:
    suc=[]
    for u in que:
        for v in adj[u]:
            if a[v]!=0:
                continue
            a[v]=u
            suc.append(v)
    que=suc

#print(N,M)
#print(adj)
#print(a)

ok=True
ans=[]
for i in range(2,N+1):
    if a[i]==0:
        ok=False
        break
    ans.append(a[i])

if not ok:
    print('No')
else:
    print('Yes')
    for x in ans:
        print(x)

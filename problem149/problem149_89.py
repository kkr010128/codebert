import itertools
N,M,X=map(int,input().split())
C=[0 for i in range(N)]
A=[[0 for j in range(M)]for i in range(N)]
for i in range(N):
    line=list(map(int,input().split()))
    C[i]=line[0]
    for j in range(M):
        A[i][j]=line[j+1]

ans=sum(C)+1
for seq in itertools.product(range(2),repeat=N):
    R=[0 for i in range(M)]
    cost=0
    for i in range(N):
        if seq[i]==0:
            continue
        cost+=C[i]
        for j in range(M):
            R[j]+=A[i][j]
    if min(R)>=X:
        ans=min(ans,cost)
if ans==sum(C)+1:
    print(-1)
else:
    print(ans)

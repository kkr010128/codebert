N,M,X=map(int,input().split())
C=[list(map(int,input().split())) for _ in range(N)]

mx=10**9
ans=mx
def dfs(i,tt,level):
    global ans
    if i==N:
        return
    tt+=C[i][0]
    lev=[]
    for j in range(M):
        lev.append(level[j]+C[i][j+1])
    ok=True
    for x in lev:
        if x<X:
            ok=False
            break
    if ok:
        ans=min(ans,tt)
    for j in range(i+1,N):
        dfs(j,tt,lev)
        

for i in range(N):
    dfs(i,0,[0]*M)

if ans==mx:
    print(-1)
else:
    print(ans)

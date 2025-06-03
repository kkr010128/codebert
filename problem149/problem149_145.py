N,M,X=map(int,input().split())
C=[list(map(int,input().split())) for _ in range(N)]

ans=inf=float('inf')
def dfs(idx,tt,l):
    global ans
    for i in range(idx,N):
        ntt=tt+C[i][0]
        nl=[l[j]+C[i][j+1] for j in range(M)]
        for x in nl:
            if x<X: break
        else:
            ans=min(ans,ntt)
        dfs(i+1,ntt,nl)
        
dfs(0,0,[0]*M)

print(ans if ans<inf else -1)

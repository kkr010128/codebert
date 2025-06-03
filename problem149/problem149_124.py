N,M,X=map(int,input().split())
C=[[*map(int,input().split())] for _ in range(N)]

ans=inf=float('inf')
for perm in range(1,1<<N):
    tt,lvls=0,[0]*M
    for i in range(N):
        if perm&(1<<i)==0:
            continue
        tt+=C[i][0]
        for j in range(M):
            lvls[j]+=C[i][j+1]
        for j in range(M):
            if lvls[j]<X:
                break
        else:
            ans=min(ans,tt)
            break

print(ans if ans<inf else -1)

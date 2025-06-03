H, W = list(map(int, input().split()))
S =[list(input()) for _ in range(H)]
N=H*W
INF=float('inf')
L=[[INF]*N for _ in range(N)]
for i in range(N):
    h=i//W
    w=i%W
    # print(i,h,w)
    if S[h][w]=='.':
        L[i][i]=0
    if w>0 and S[h][w-1]=='.':
        L[i][i-1]=1
    if w<W-1 and S[h][w+1]=='.':
        L[i][i+1]=1
    if h>0 and S[h-1][w]=='.':
        L[i][i-W]=1
    if h<H-1 and S[h+1][w]=='.':
        L[i][i+W]=1
# print(L)

for i in range(N):
    via=L[i]
    if via[i]==INF:
        continue
    for j in range(N):
        st=L[j]
        if st[j]==INF:
            continue
        for k in range(N):
            L[j][k]=min(st[i]+via[k], st[k])
# print(L)
ans=0
for i in range(N):
    for j in range(N):
        if L[i][j]!=INF:
            ans=max(ans,L[i][j])
print(ans)
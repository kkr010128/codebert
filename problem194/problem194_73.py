h,w=map(int, input().split())
s=[list(input()) for _ in range(h)]

dx=[1,0]
dy=[0,1]

dp=[[10**9]*(w) for _ in range(h)]
if s[0][0]=='#':
    dp[0][0]=1
else:
    dp[0][0]=0

for i in range(h):
    for j in range(w):
        for d in range(2):
            new_i=i+dx[d]
            new_j=j+dy[d]
            if h<=new_i or w<=new_j:
                continue
            add=0
            if s[new_i][new_j]=='#' and s[i][j]=='.':
                add=1
            dp[new_i][new_j]=min(dp[new_i][new_j], dp[i][j]+add)

print(dp[-1][-1])

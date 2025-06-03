H,W=list(map(int,input().split()))
l=[list(input()) for i in range(H)]
inf=10**9
DP=[[inf]*W for i in range(H)]
DP[0][0]=0 if l[0][0]=="." else 1
for i in range(H):
   for j in range(W):
      if i>0:
         DP[i][j]=min(DP[i][j],DP[i-1][j]+1) if l[i-1][j] == "." and l[i][j]=="#" else min(DP[i][j],DP[i-1][j])
      if j>0:
         DP[i][j]=min(DP[i][j],DP[i][j-1]+1) if l[i][j-1] == "." and l[i][j]=="#" else min(DP[i][j],DP[i][j-1])
print(DP[H-1][W-1])
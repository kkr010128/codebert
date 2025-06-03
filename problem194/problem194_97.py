# A - Range Flip Find Route
h,w=map(int,input().split())
s=[input() for i in range(h)]
inf=10**18
dp=[[inf]*(w+1) for i in range(h+1)]
if s[0][0]=="#":
  dp[0][0]=1
else:
  dp[0][0]=0

for i in range(h):
  for j in range(w):
    for y,x in ([1,0],[0,1]):
      ni,nj=i+y,j+x
      if ni>=h or nj>=w:continue
      c=0
      if s[ni][nj]=="#" and s[i][j]==".":c=1
      dp[ni][nj]=min(dp[ni][nj],dp[i][j]+c)

print(dp[h-1][w-1])

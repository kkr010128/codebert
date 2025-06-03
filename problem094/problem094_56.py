import sys
input=sys.stdin.readline
R,C,k=map(int,input().split())
A=[[0]*C for i in range(R)]
for i in range(k):
  r,c,v=map(int,input().split())
  A[r-1][c-1]=v
dp0=[[0]*(C+1) for i in range(R+1)]
dp1=[[0]*(C+1) for i in range(R+1)]
dp2=[[0]*(C+1) for i in range(R+1)]
dp3=[[0]*(C+1) for i in range(R+1)]
for i in range(1,R+1):
  for j in range(1,C+1):
    V=A[i-1][j-1]
    dp0[i][j]=max(dp0[i-1][j],dp1[i-1][j],dp2[i-1][j],dp3[i-1][j],dp0[i][j-1])
    dp1[i][j]=max(dp0[i][j]+V,dp1[i][j-1])
    dp2[i][j]=max(dp1[i][j-1]+V,dp2[i][j-1])
    dp3[i][j]=max(dp2[i][j-1]+V,dp3[i][j-1])
print(max(dp0[-1][-1],dp1[-1][-1],dp2[-1][-1],dp3[-1][-1]))
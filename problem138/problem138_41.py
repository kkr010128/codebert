import sys
import  math
import fractions
from collections import defaultdict
stdin = sys.stdin
     
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

mod=998244353

N,S=nm()
A=nl()


dp=[[0]*3001  for _ in range(3001)]#i i番目 j和がj
dp[0][A[0]]=1
dp[0][0]=2
for i in range(1,N):
    for j in range(0,3001):
        if(0<=(j-A[i])):
            dp[i][j]=dp[i-1][j-A[i]]+2*dp[i-1][j]
        else:
            dp[i][j]=2*dp[i-1][j]
        dp[i][j]%=mod

ans=dp[N-1][S]
print(ans%mod)
N=int(input())
*A,=map(int, input().split())
B=[(i+1,a) for i,a in enumerate(A)]
from operator import itemgetter
B.sort(reverse=True, key=itemgetter(1))

dp = [[-1] * (N+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(1,N+1):
    idx, act = B[i-1]
    for j in range(i+1):
        k = i-j
        if 0<j: dp[j][k] = max(dp[j][k], dp[j-1][k] + act * abs(idx-j))
        if 0<k: dp[j][k] = max(dp[j][k], dp[j][k-1] + act * abs(idx-(N-k+1)))

ans=0
for j in range(N+1):
    ans = max(ans, dp[j][N-j])
print(ans)


import sys
input = sys.stdin.readline
N,K = map(int,input().split())
MOD = 998244353
dp = [0 for _ in range(N+1)]
dp[1] = 1
R = [tuple(map(int,input().split())) for _ in range(K)]
S = [0 for _ in range(K)]
for i in range(2, N+1):
	s = 0
	for k in range(K):
		S[k] += dp[max(0, i - R[k][0])] - dp[max(0, i - R[k][1] - 1)]
		S[k] %= MOD
		s = (s + S[k]) % MOD
	dp[i] = s
print(dp[N])
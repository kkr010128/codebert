MOD = 998244353

N,K = map(int,input().split())

l = []
dp = [0]*N
sdp = [0]*(N+1)
for i in range(K):
    L,R = map(int,input().split())
    l.append([L,R])
dp[0] = 1
sdp[1] = 1

for i in range(1,N):
    for L, R in l:
        dp[i] += sdp[max(0,i - L+1)] - sdp[max(0,i - R)]
        dp[i] %= MOD
    sdp[i+1] = sdp[i] + dp[i]
    sdp[i+1] %= MOD

print(dp[N-1])
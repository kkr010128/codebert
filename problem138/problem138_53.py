
def solve(N,S,A):
    dp = [[0]*(S+1) for _ in range(N+1)]
    dp[0][0] = 1
    mod = 998244353
    for i, a in enumerate(A, 1):
        for s in range(S+1):
            if s-a >= 0:
                dp[i][s] = (dp[i-1][s] * 2 + dp[i-1][s-a]) % mod
            else:
                dp[i][s] = dp[i-1][s] * 2 % mod
    print(dp[N][S])

N, S = map(int, input().split())
A = list(map(int, input().split()))
solve(N,S,A)

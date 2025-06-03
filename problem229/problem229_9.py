def solve():
    H, N = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [float('inf')]*(H+10**4)
    dp[0] = 0
    for h in range(1,H+10**4):
        for i in range(N):
            if A[i][0]<=h:
                dp[h] = min(dp[h],dp[h-A[i][0]]+A[i][1])
    ans = min(dp[H:])
    return ans
print(solve())
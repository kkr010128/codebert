N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

dp = [[0]*3 for _ in range(N+1)]
for i in range(1, N+1):
    if i <= K:
        dp[i][0] = int(T[i-1]=='s') * R
        dp[i][1] = int(T[i-1]=='p') * S
        dp[i][2] = int(T[i-1]=='r') * P
    else:
        dp[i][0] = max(dp[i-K][1], dp[i-K][2]) + int(T[i-1]=='s') * R
        dp[i][1] = max(dp[i-K][0], dp[i-K][2]) + int(T[i-1]=='p') * S
        dp[i][2] = max(dp[i-K][0], dp[i-K][1]) + int(T[i-1]=='r') * P

ans = 0
for d in dp[-K:]:
    ans += max(d)
print(ans)
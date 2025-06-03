N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
divided_T = [[] for _ in range(K)]
for i in range(N):
    divided_T[i%K].append(T[i])
ans = 0
for target in divided_T:
    dp = [[0]*3 for _ in range(len(target))]
    dp[0][0] = R if target[0] == 's' else 0
    dp[0][1] = P if target[0] == 'r' else 0
    dp[0][2] = S if target[0] == 'p' else 0
    for i in range(1,len(target)):
        dp[i][0] = max(dp[i-1][1],dp[i-1][2]) + (R if target[i] == 's' else 0)
        dp[i][1] = max(dp[i-1][0],dp[i-1][2]) + (P if target[i] == 'r' else 0)
        dp[i][2] = max(dp[i-1][1],dp[i-1][0]) + (S if target[i] == 'p' else 0)
    ans += max(dp[-1])
print(ans)
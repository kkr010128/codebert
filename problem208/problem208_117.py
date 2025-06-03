N,M = map(int, input().split())

dp = [-1] * N
for i in range(M):
    s, c = map(int, input().split())
    s -= 1
    if dp[s] != -1 and dp[s] != c:
        print(-1)
        exit()
    dp[s] = c

if N != 1:
    if dp[0] == 0:
        print(-1)
        exit()

    if dp[0] == -1:
        dp[0] = 1

    for i in range(1, N):
        if dp[i] == -1:
            dp[i] = 0

else:
    if dp[0] == -1:
        dp[0] = 0

print(''.join(map(str, dp)))
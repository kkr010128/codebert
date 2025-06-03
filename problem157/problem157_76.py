n = int(input())
a = list(map(int, input().split()))

ans = 0
dp = dict()

for i in range(n):
    a_p = a[i] + i+1
    a_m = i+1 -a[i]
    if a_p in dp:
        dp[a_p] = dp[a_p] + 1
    else:
        dp[a_p] = 1
    if a_m in dp:
        ans = ans + dp[a_m]


print(ans)
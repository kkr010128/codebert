N = int(input())
A = list(map(int, input().split()))
MOD = 10**9+7

ans = 1
dp = [0]*3
for a in A:
    cnt = 0
    for i in range(3):
        if a == dp[i]:
            cnt += 1
    for i in range(3):
        if a == dp[i]:
            dp[i] += 1
            break
    ans = ans*cnt % MOD
print(ans)

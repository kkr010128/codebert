n, t = map(int, input().split())
ab = []
for _ in range(n):
    ab.append(list(map(int, input().split())))

ab.sort(key=lambda x:x[0])

dp = [-1]*(t+1)
dp[0] = 0

for a, b in ab:
    tmp = dp[:]
    for i in range(t):
        if dp[i] >= 0 and dp[i]+b > tmp[min(i+a, t)]:
            tmp[min(i+a, t)] = dp[i]+b
    dp = tmp
print(max(dp))
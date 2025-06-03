H,N = map(int,input().split())
inf = 1000000000
dp = [inf for _ in range(20001)]
magics = []
dp[0] = 0
for i in range(N):
    magic = list(map(int,input().split()))
    magics.append(magic)
for j in range(10001):
    for k in magics:
        dp[j+k[0]] = min(dp[j]+k[1],dp[j+k[0]])
ans = dp[H:]
print(min(ans))
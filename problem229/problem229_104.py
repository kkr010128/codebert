h, n = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(n)]
#(a,b):=(ダメージ,消費魔力)

dp = [float('inf')] * (h + 1)
dp[0] = 0

for i in range(h + 1):
    for j in range(n):
        if dp[i] == float('inf'):continue
        temp_a = i + ab[j][0] if i + ab[j][0] < h else h
        temp_b = dp[i] + ab[j][1]

        dp[temp_a] = min(dp[temp_a], temp_b)

print(dp[-1])
#print(dp)

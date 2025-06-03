import sys
input = sys.stdin.readline
h,n = map(int,input().split())
ab = [list(map(int,input().split()))for i in range(n)]
amx = 0
for i in range(n):
    if amx < ab[i][0]:
        amx = ab[i][0]
#dp[i] = モンスターの削る体力がiの時の魔力の消費の最小値
dp = [float('inf')]*(amx + h + 1)
dp[0] = 0
for i in range(amx + h + 1):
    for m in ab:
        if i-m[0] >= 0:
            dp[i] = min(dp[i], dp[i-m[0]] + m[1])

ans = float('inf')
for i in range(h,amx + h + 1):
    ans = min(ans, dp[i])

print(ans)

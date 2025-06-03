import sys
input = sys.stdin.readline
H,N = map(int,input().split())
spells = [list(map(int,input().split())) for i in range(N)]
INF = 10**10
dp = [INF]*(H+1)
dp[0] = 0
for use in spells:
    damage = use[0]
    mp = use[1]
    for i in range(1,H+1):
        dp[i] = min(dp[max(0,i-damage)] + mp, dp[i])
print(dp[-1])

x = int(input())

dp = [True] + [False] * (x+110)

for i in range(len(dp)):
    if not dp[i]: continue
    for food in range(100, 106):
        if i+food >= len(dp): continue
        dp[i+food] = True

if dp[x]: print(1)
else: print(0)
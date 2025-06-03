H, N = map(int, input().split())
List = [list(map(int, input().split())) for _ in range(N)]

inf = 10 ** 9
dp = [0] + [inf] * H

for h in range(1, H + 1):
    for n in range(1, N + 1):
        a, b = List[n - 1]
        ref = h - a
        if ref < 0: ref = 0
        dp[h] = min(dp[h], dp[ref] + b)
        

print(dp[H])

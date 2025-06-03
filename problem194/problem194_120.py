import sys
import fractions

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

H, W = lr()
dp = [[0 for _ in range(W)] for _ in range(H)]
masu = [sr() for _ in range(H)]
dp[0][0] = 1 if masu[0][0] == "#" else 0
for h, m in enumerate(masu):
    for w, s in enumerate(m):
        if w == 0 and h == 0:
            continue
        if w == 0:
            if masu[h-1][w] != s and s == "#":
                dp[h][w] += dp[h-1][w] + 1
            else:
                dp[h][w] += dp[h-1][w]
            continue
        if h == 0:
            if masu[h][w-1] != s and s == "#":
                dp[h][w] += dp[h][w-1] + 1
            else:
                dp[h][w] += dp[h][w-1]
            continue
        if masu[h-1][w] != s and s == "#":
            cand1 = dp[h][w] + dp[h-1][w] + 1
        else:
            cand1 = dp[h][w] + dp[h-1][w]
        if masu[h][w-1] != s and s == "#":
            cand2 = dp[h][w] + dp[h][w-1] + 1
        else:
            cand2 = dp[h][w] + dp[h][w-1]
        dp[h][w] = min(cand1, cand2)
print(dp[H-1][W-1])

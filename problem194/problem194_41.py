INF = 10**9
def solve(h, w, s):
    dp = [[INF] * w for r in range(h)]
    dp[0][0] = int(s[0][0] == "#")
    for r in range(h):
        for c in range(w):
            for dr, dc in [(-1, 0), (0, -1)]:
                nr, nc = r+dr, c+dc
                if (0 <= nr < h) and (0 <= nc < w):
                    dp[r][c] = min(dp[r][c], dp[nr][nc] + (s[r][c] != s[nr][nc]))
    return (dp[h-1][w-1] + 1) // 2

h, w = map(int, input().split())
s = [input() for r in range(h)]
print(solve(h, w, s))

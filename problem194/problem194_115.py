import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = [list("." + input()) for _ in range(H)]

    dp = [[f_inf] * (W + 1) for _ in range(H)]
    dp[0][0] = 0

    for h in range(H):
        for w in range(W + 1):
            if w == 0:
                if h != 0:
                    continue
                next_h, next_w = h, w + 1
                if grid[h][w] == "." and grid[next_h][next_w] == "#":
                    dp[next_h][next_w] = min(dp[next_h][next_w], dp[h][w] + 1)
                elif grid[h][w] == "." and grid[next_h][next_w] == "#":
                    dp[next_h][next_w] = min(dp[next_h][next_w], dp[h][w] + 1)
                else:
                    dp[next_h][next_w] = min(dp[next_h][next_w], dp[h][w])
            else:
                for dh, dw in [(1, 0), (0, 1)]:
                    next_h, next_w = h + dh, w + dw
                    if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W + 1:
                        continue
                    if grid[h][w] == "." and grid[next_h][next_w] == "#":
                        dp[next_h][next_w] = min(dp[next_h][next_w], dp[h][w] + 1)
                    elif grid[h][w] == "." and grid[next_h][next_w] == "#":
                        dp[next_h][next_w] = min(dp[next_h][next_w], dp[h][w] + 1)
                    else:
                        dp[next_h][next_w] = min(dp[next_h][next_w], dp[h][w])
    print(dp[-1][-1])


if __name__ == '__main__':
    resolve()

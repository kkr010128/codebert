import sys


def main():
    dp = [[0] * W for _ in range(H)]

    for y in range(H):
        for x in range(W):
            if x == 0 and y == 0:
                if s[0][0] == "#":
                    dp[0][0] = 1
            elif x == 0:
                if s[y][x] == "#" and s[y - 1][x] == ".":
                    dp[y][x] = dp[y - 1][x] + 1
                else:
                    dp[y][x] = dp[y - 1][x]
            elif y == 0:
                if s[y][x] == "#" and s[y][x - 1] == ".":
                    dp[y][x] = dp[y][x - 1] + 1
                else:
                    dp[y][x] = dp[y][x - 1]
            else:
                if s[y][x] == "#" and s[y][x - 1] == "." and s[y - 1][x] == ".":
                    dp[y][x] = min(dp[y][x - 1], dp[y - 1][x]) + 1
                elif s[y][x] == "#" and s[y][x - 1] == ".":
                    dp[y][x] = min(dp[y][x - 1] + 1, dp[y - 1][x])
                elif s[y][x] == "#" and s[y - 1][x] == ".":
                    dp[y][x] = min(dp[y][x - 1], dp[y - 1][x] + 1)
                else:
                    dp[y][x] = min(dp[y][x - 1], dp[y - 1][x])

    print(dp[-1][-1])


if __name__ == "__main__":
    H, W = map(int, sys.stdin.readline().split())
    s = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
    main()
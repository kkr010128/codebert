def main():
    H, W = (int(i) for i in input().split())
    c = [input() for i in range(H)]
    dp = [[10**3]*W for _ in range(H)]
    if c[0][0] == "#":
        dp[0][0] = 1
    else:
        dp[0][0] = 0
    for h in range(H):
        for w in range(W):
            if c[h][w] == ".":
                if w < W-1 and c[h][w+1] == ".":
                    dp[h][w+1] = min(dp[h][w+1], dp[h][w])
                elif w < W-1 and c[h][w+1] == "#":
                    dp[h][w+1] = min(dp[h][w+1], dp[h][w] + 1)
                if h < H-1 and c[h+1][w] == ".":
                    dp[h+1][w] = min(dp[h+1][w], dp[h][w])
                elif h < H-1 and c[h+1][w] == "#":
                    dp[h+1][w] = min(dp[h+1][w], dp[h][w] + 1)
            else:
                if w < W-1:
                    dp[h][w+1] = min(dp[h][w+1], dp[h][w])
                if h < H-1:
                    dp[h+1][w] = min(dp[h+1][w], dp[h][w])
    print(dp[H-1][W-1])
    # print(*dp, sep="\n")


if __name__ == '__main__':
    main()

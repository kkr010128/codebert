import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(int, input().split()))

def main():
    INF = 10**9
    H, W = input_nums()
    ss = [input() for _ in range(H)]
    dp = [[0]*W for _ in range(H)]
    if ss[0][0] == '#': dp[0][0] = 1
    for h in range(H):
        for w in range(W):
            if (h, w) == (0, 0): continue
            u = l = INF
            if h-1>=0:
                u = dp[h-1][w]
                if ss[h][w] == '#' and ss[h-1][w] == '.': u += 1
            if w-1>=0:
                l = dp[h][w-1]
                if ss[h][w] == '#' and ss[h][w-1] == '.': l += 1
            dp[h][w] = min(u, l)
    print(dp[H-1][W-1])

if __name__ == '__main__':
    main()


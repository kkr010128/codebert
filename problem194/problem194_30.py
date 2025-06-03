import sys
import collections

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    H, W = [int(x) for x in input().split()]
    S = [list(input().strip()) for _ in range(H)]

    dp = [[10 ** 9] * W for _ in range(H)]
    dp[0][0] = int(S[0][0] == '#')

    for j in range(H):
        for i in range(W):
            if j != H - 1:
                dp[j + 1][i] = min(dp[j + 1][i], dp[j][i] + int(S[j + 1][i] == '#' and S[j][i] == '.'))
            if i != W - 1:
                dp[j][i + 1] = min(dp[j][i + 1], dp[j][i] + int(S[j][i + 1] == '#' and S[j][i] == '.'))
    print(dp[-1][-1])


if __name__ == '__main__':
    main()

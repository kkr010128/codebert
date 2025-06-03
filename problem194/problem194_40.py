#!/usr/bin/env python3
from queue import Queue

def II(): return int(input())
def MII(): return map(int, input().split())
def LII(): return list(map(int, input().split()))


def main():
    H, W = MII()
    S = [input() for _ in range(H)]
    dp = [[10**9] * W for _ in range(H)]

    dp[0][0] = (S[0][0] == '#') + 0
    for i in range(H):
        for j in range(W):
            a = dp[i-1][j]
            b = dp[i][j-1]

            if S[i-1][j] == '.' and S[i][j] == '#':
                a += 1
            if S[i][j-1] == '.' and S[i][j] == '#':
                b += 1
            
            dp[i][j] = min(dp[i][j], a, b)
                 
    print(dp[H-1][W-1])


if __name__ == '__main__':
    main()
#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N,S=map(int, input().split())
    A = list(map(int,input().split()))
    mod = 998244353
    dp = [[0]*(S+1) for i in range(N+1)]
    dp[0][0]=1
    for i in range(N):
        vi = A[i]
        for j in range(S+1):
            dp[i+1][j] += 2 * dp[i][j]
            dp[i+1][j] %= mod
            if j+vi<=S:
                dp[i+1][j+vi] += dp[i][j]
                dp[i+1][j+vi] %= mod

    print(dp[N][S])

if __name__ == '__main__':
    main()

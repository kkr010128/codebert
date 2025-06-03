def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math
    #from math import gcd

    inf = 10**17
    #mod = 10**9 + 7

    N,M,L = map(int, input().split())
    dp = [[inf]*N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
    for _ in range(M):
        a,b,c = map(int, input().split())
        dp[a-1][b-1] = c
        dp[b-1][a-1] = c

    #kを経由してiからjに行く行き方を考える
    #これで上手く行くのは与えられた辺の和しか考えていないため
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[j][i] = dp[i][k]+dp[k][j]

    dp2 =  [[inf]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if dp[i][j] <= L:
                dp2[i][j] = dp2[j][i] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dp2[i][j] > dp2[i][k] + dp2[k][j]:
                    dp2[i][j] = dp2[j][i] = dp2[i][k]+dp2[k][j]

    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        if dp2[s-1][t-1] == inf:
            print(-1)
        else:
            print(dp2[s-1][t-1]-1)

if __name__ == '__main__':
    main()
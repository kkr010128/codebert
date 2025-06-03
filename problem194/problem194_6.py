# -*- coding: utf-8 -*-
import sys
# from collections import defaultdict, deque
# from math import sqrt, gcd, factorial, tan, pi, sin, cos
def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline()[:-1]


def solve():
    n, m = [int(x) for x in input().split()]
    dp = [[float('inf') for _ in range(m)] for _ in range(n)]
    s = []
    for i in range(n):
        s.append(input())
        
    for i in range(n):
        for j in range(m):
            c = int(s[i][j] != '.')
            if i == 0 and j == 0:
                dp[i][j] = c
            if i:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + c * (s[i-1][j] != s[i][j]))
            if j:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + c * (s[i][j-1] != s[i][j]))
    # for r in dp:
    #     print(*r)
    print(dp[n-1][m-1])
        




t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()



"""
1 -> (1, 2) -> (2 ** 3, 3) -> (3, 1)

"""


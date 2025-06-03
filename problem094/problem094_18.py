import bisect
import collections
import copy
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
MOD = 10**9+7

R,C,K = map(int,input().split())

item = [[0]*C for _ in range(R)]
for i in range(K):
    r,c,v = map(int,input().split())
    item[r-1][c-1] = v
#print(item)

dp = [[0]*4 for _ in range(C)]
preview = [[0]*4 for _ in range(C)]

for i in range(R):
    for j in range(C):
        for k in range(1,4):
            #print(i,j,k)
            if k == 1:
                if i != 0:
                    if j != 0:
                        dp[j][k] = max(dp[j-1][k], dp[j-1][k-1] + item[i][j], max(preview[j]) + item[i][j])
                    else:
                        dp[j][k] = max(0, 0 + item[i][j], max(preview[j]) + item[i][j])
                else:
                    if j != 0:
                        dp[j][k] = max(dp[j-1][k], dp[j-1][k-1] + item[i][j])
                    else:
                        dp[j][k] = max(0, 0 + item[i][j])


            else:
                if j != 0:
                    dp[j][k] = max(dp[j-1][k], dp[j-1][k-1] + item[i][j])
                else:
                    dp[j][k] = max(0, 0 + item[i][j])

            #print(dp)
    preview = dp
print(max(dp[C-1]))
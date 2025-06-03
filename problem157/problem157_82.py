# https://atcoder.jp/contests/abc166/tasks/abc166_e

"""
変数分離すれば互いに独立なので、
連想配列でO(N)になる。
"""


import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
A = list(map(int, input().split()))

P = (j+1-A[j] for j in range(N))
M = (i+1+A[i] for i in range(N))

dic = Counter(P)

res = 0
for m in M:
    res += dic.get(m,0)

print(res)
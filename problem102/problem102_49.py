# coding:UTF-8
import sys
from math import factorial

MOD = 10 ** 9 + 7
INF = float('inf')

N, K = list(map(int, input().split()))     # スペース区切り連続数字
A = list(map(int, input().split()))     # スペース区切り連続数字

for i in range(K, N):
    r = i - K
    l = i
    if A[r] >= A[l]:
        print("No")
    else:
        print("Yes")

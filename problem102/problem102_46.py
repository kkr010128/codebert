import numpy as np

# 解説みた
N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(K, N):
    if A[i] / A[i - K] > 1:
        print("Yes")
    else:
        print("No")

"""
・書き始める前に式変形等考える
・判定分を吟味する。（実際の数、今回でいうと積、で比較しない）
"""

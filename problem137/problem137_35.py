# -*- coding: utf-8 -*-
# 整数の入力
import math
import numpy as np

N = int(input())
A = []
B = []
for i in range(N):
    t = list(map(int, input().split()))
    A.append(t[0])
    B.append(t[1])
A.sort()
B.sort()

if N % 2 == 0:
    i = N // 2
    j = N // 2 - 1
    a = A[j] + A[i]
    b = B[j] + B[i]
    print(b - a + 1)
else:
    i = N // 2
    a = B[i] - A[i] + 1

    print(a)


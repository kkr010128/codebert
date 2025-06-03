# 入力
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

# ライブラリ
import itertools
l = [i+1 for i in range(n)]
perms = itertools.permutations(l, n)

# 処理
a = 0
b = 0
for i, perm in enumerate(perms):
    perm = list(perm)
    if perm == p:
        a = i
    if perm == q:
        b = i

import numpy as np
print(np.abs(a-b))
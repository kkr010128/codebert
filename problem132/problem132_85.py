import numpy as np
from numba import njit

@njit #処理の並列化_これがない場合は'TLE'
def imos(n, a):
    l=np.zeros((n+1), dtype = np.int64)

    for i, x in enumerate(a):# x_光の強さ_これで照射範囲が決まる
        left = max(0, i - x) #StartIndex_照らせる範囲
        right = min(n, i + x + 1) #EndIndex + 1_照らせる範囲
        l[left] += 1 # 各々を'+1'と'-1'で表し...
        l[right] -= 1

    return np.cumsum(l)[:n] # 累積和をとる_cumulative sum

n, k = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(k):
    a = imos(n, a)
    if a.min() == n: # すべての要素が最大値'n'になるとbreak
        break

print(*a)

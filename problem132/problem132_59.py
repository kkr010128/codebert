import numpy as np
from numba import njit

@njit #処理の並列化_これがない場合は'TLE'
def imos(n, a):
    
    l=np.zeros((n+1), dtype = np.int64)

    for i in range(n):
        ai = a[i] # 光の強さ_これにより照らせる範囲が決まる
        start = max(0, i - ai) #StartIndex_照らせる範囲
        end = min(n, i + ai + 1) #EndIndex + 1_照らせる範囲
        l[start] += 1 # 各々を'+1'と'-1'で表し...
        l[end] -= 1
    return np.cumsum(l)[:n] # 累積和をとる_cumulative sum

n, k = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(k):
    a = imos(n, a)
    if a.min() == n: # すべての要素が最大値'n'になるとbreak
        break

print(*a)

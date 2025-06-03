# ac
import sys
import numpy as np
from numba import njit

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit('(i8[::1],)', cache=True)
def update(a):
    n = len(a)
    b = np.zeros_like(a)       # aと同じ形状の配列を生成(https://deepage.net/features/numpy-zeros.html)
    for i, x in enumerate(a):  # enumerateはindex, valueを返す
        l = max(0, i - x)      # lampの照らす範囲の下限（左側）
        r = min(n - 1, i + x)  # lampの上限（右側）
        b[l] += 1              # 以下imos法
        if r + 1 < n:          # r+1はx=nの時（最後のサイクル）r+1=nでindexの指定に失敗するから弾く（indexは0~n-1）
            b[r + 1] -= 1
    b = np.cumsum(b)           # bの要素の累積和（フィボナッチ数列みたいな）（imos法の締め）
    return b


n, k = map(int, readline().split())
a = np.array(read().split(), np.int64)

k = min(k, 41)                 # 今回の制限範囲のnなら41回も試行すればaの値が全て上限に達するのでそれ以上の試行は不要（解説PDF）
for _ in range(k):
    a = update(a)
print(' '.join(map(str, a)))   # joinメソッドはstrを''で区切って連結する
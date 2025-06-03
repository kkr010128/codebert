# -*- coding: utf-8 -*-
import itertools
N, K = map(int, input().split())
a = [0] * (N+1)
for i in range(N+1):
  a[i] = i

max_total = 0
min_total = 0
ans = 0
for k in range(K, N+2):
  # 和の最大(10**100 は無視): 大きい順にk個選んだ場合
  max_total = k * ((N-k+1) + N) // 2

  # 和の最小(10**100 は無視): 小さい順にk個選んだ場合
  min_total = k * (0 + (k-1)) // 2

  # 最小と最大の間は全パターン取り得るので差が個数になる
  ans += (max_total - min_total + 1)

print(ans % (10**9 + 7))
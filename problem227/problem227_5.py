# -*- coding: utf-8 -*-
N, K = map(int, input().split())
H = list(map(int, input().split()))
H = sorted(H, reverse=True)
total = 0
for i in range(K, N):
  total += H[i]
print(total)
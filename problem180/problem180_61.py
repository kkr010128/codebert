# -*- coding: utf-8 -*-

N, K = map(int, input().split())

remainder = N % K

if remainder > K / 2:
  print(abs(remainder - K))
else:
  print(remainder)
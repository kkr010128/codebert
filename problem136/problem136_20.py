# -*- codinf: utf-8 -*-
import math
N = int(input())
# 素因数分解
n = N
i = 2
f = {} # keyが素因数、valueが素因数の数
while i * i <= n:
  count = 0
  while n % i == 0:
    count += 1
    f[i] = count
    n /= i
  i += 1
if 1 < n:
  f[n] = 1

if len(f) == 0:
  print(0)
  exit()

count = 0
for v in f.values():
  d = 1
  while v > 0:
    v -= d
    if v >= 0:
      count += 1
    d += 1
print(count)
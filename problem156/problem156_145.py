# -*- coding: utf-8 -*-
X = int(input())

# A**5 - (A-1)**5 = X = 10**9(Xの最大) となるAが
# Aの最大値となる(それ以上Aが大きくなると、Xは上限値を超える)
# → 最大となるAは120

for A in range(-120, 120 + 1):
  for B in range(-120, 120):
    if A**5 - B**5 == X:
      print("{} {}".format(A, B))
      exit()
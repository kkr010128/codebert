# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 16:48:51 2020

@author: Aruto Hosaka
"""


import math
import collections

K = int(input())
ans = 0
g = []
for a in range(K):
  for b in range(K):
      g.append(math.gcd(a+1, b+1))
G = collections.Counter(g)

for k in range(K):
  for c in range(K):
      ans += math.gcd(k+1, c+1)*G[k+1]
      
print(ans)
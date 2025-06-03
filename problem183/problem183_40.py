#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n = int(input())
for i in range(2,int(n**.5) + 1):
  if n % i == 0:
    tmp = n
    while tmp % i==0:
      tmp //= i
    if (tmp-1) % i == 0:ans += 1

    if n//i != i:
      tmp = n;i = n//i
      while tmp % i==0:
        tmp //= i
      if (tmp-1) % i == 0:ans += 1

for i in range(2,int((n-1)**.5 )+ 1):
  if (n-1) % i == 0:
    if (n-1) // i == i: ans += 1
    else: ans += 2
# print(ans)
print(ans+1 + int(n != 2))
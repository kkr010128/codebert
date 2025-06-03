#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n,mod = map(int,input().split())
S = list(map(int,input()))
if mod == 2:
  for i in range(n):
    if S[i] % 2 == 0:
      ans += i+1
elif mod == 5:
  for i in range(n):
    if S[i] % 5 == 0:
      ans += i + 1
else:
  tenpow = 1
  for i in range(n-1,-1,-1):
    S[i] = S[i] * tenpow % mod
    tenpow = tenpow * 10 % mod
  acum = [0]*(n+1)
  for i in range(n):
    acum[i+1] = (acum[i]+S[i]) % mod
  C = collections.Counter(acum)
  for key,item in C.items():
    ans += (item-1) * item //2


print(ans)

# -*- coding: utf-8 -*-
N = int(input())
X = list(map(int, input().split()))

min_x = X[0]
max_x = X[0]
for i in range(N):
  if X[i] > max_x: max_x = X[i]
  if X[i] < min_x: min_x = X[i]

ans = 10000000
for p in range(min_x, max_x+1):
  ans_p = 0
  for x in X:
    ans_p += (x-p)**2
  if ans > ans_p: ans = ans_p

print(ans)
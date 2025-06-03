# -*- coding: utf-8 -*-
n, k = map(int, input().split())
a = list(map(int, input().split()))
for j in range(k):
  b = [0] * (n + 1)
  for i in range(n):
    left_edge = max(0, i-a[i])
    right_edge = min(i + a[i] + 1, n)
    b[left_edge] += 1
    b[right_edge] -= 1
  for i in range(1, n+1):
    b[i] = b[i] + b[i-1]
  b.pop(n)
  if a == b:
    break
  a = b.copy()
print(' '.join(str(b[i]) for i in range(n)))
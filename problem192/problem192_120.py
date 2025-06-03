# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

s = [0] * N
for i in range(N):
  s[A[i]-1] += 1

total = 0
for i in range(N):
  total += s[i]*(s[i]-1) // 2

for k in range(N):
  ans = total - s[A[k]-1]*(s[A[k]-1]-1)//2 + (s[A[k]-1]-1)*((s[A[k]-1]-1)-1) // 2
  print(ans)
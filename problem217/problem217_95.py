# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

ans = "APPROVED"
for a in A:
  if a % 2 == 0:
    if a % 3 == 0 or a % 5 == 0:
      pass
    else:
      ans = "DENIED"
      break
print(ans)
# -*- coding: utf-8 -*-
A, B, C, D = map(int, input().split())

i = 0
while A > 0 and C > 0:
  i += 1
  if i % 2 == 1:
    # 高橋くんの攻撃
    C -= B
  else:
    # 青木くんの攻撃
    A -= D

if C <= 0:
  print("Yes")
else:
  print("No")
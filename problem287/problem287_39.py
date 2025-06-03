#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
r = False
for i in range(1,10):
  if n % i == 0:
    if n // i < 10:
      r = True
      break

if r:
  print('Yes')
else:
  print('No')

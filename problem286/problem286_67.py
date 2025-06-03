#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b = map(int, input().split())

if a >= 1 and a <= 9 and b >= 1 and b <= 9:
  print(a*b)
else:
  print(-1)

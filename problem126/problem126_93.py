#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x = list(map(int, input().split()))
for i in range(1,6):
  if x[i-1]!=i:
    print(i)

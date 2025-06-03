#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

money = 100000

d = int(sys.stdin.read())
for i in range(d):
  money *= 1.05
  if money%1000 != 0:
    money -= money%1000
    money += 1000
print int(money)
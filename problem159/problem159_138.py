#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x = int(input())

r = 100
n=0
while True:
  n=n+1
  #r = r+int(r*0.01)
  r = r+int(r//100)
  if r >= x:
    break
print(n)

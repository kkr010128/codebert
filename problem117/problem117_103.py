#!/usr/bin/python3
# -*- coding:utf-8 -*-

import numpy

def main():
  _, _, k = map(int, input().strip().split())
  la = numpy.cumsum([0] + list(map(int, input().strip().split())))
  lb = numpy.cumsum([0] + list(map(int, input().strip().split())) + [10**9+5])
  
  def bs(x):
    s, t = 0, len(lb) - 1
    while t > s + 1:
      m = (s + t) // 2
      if lb[m] == x:
        return m
      if lb[m] > x:
        t = m
      else:
        s = m
    return s
  
  ans = 0
  for i, a in enumerate(la):
    if k - a >= 0:
      ans = max(ans, i + bs((k - a)))
  print(ans)

if __name__=='__main__':
  main()


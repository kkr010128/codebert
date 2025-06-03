# -*- coding: utf-8 -*-
import sys
from sys import stdin
import math

n, k = map(int, stdin.readline().split())
w = list([int(stdin.readline().rstrip()) for i in range(n)])

def main2():
  def is_ok():
    cnt_track = w_tmp = 0
    for w_i in w:
      w_tmp += w_i
      if w_tmp > m:
        w_tmp = w_i
        cnt_track += 1
        if cnt_track >= k:
          return 0
    return 1

  r = sum(w)
  l = max(math.ceil(r/k),max(w))
  while l < r:
    m = (l + r) // 2
    # print("%d %d %d " % (l, r, m))
    if is_ok():
      r = m
    else:
      l = m + 1
  print(r)

if __name__ == '__main__':
  main2()


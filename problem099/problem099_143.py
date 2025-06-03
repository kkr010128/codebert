#!/usr/bin python3
# -*- coding: utf-8 -*-

import bisect
n,k = map(int, input().split())
a = sorted(list(map(int, input().split())))

def cnt(x):
  ret = 0
  for ai in a:
    ret += (ai+(x-1))//x - 1
  return ret

ok, ng = a[-1], 0
while ok - ng > 1:
  nw = (ok + ng) // 2
  if cnt(nw)<=k:
    ok = nw
  else:
    ng = nw

print(ok)

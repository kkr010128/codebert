#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def gcd( a, b ):
  while b > 0:
    a, b = b, a%b
  return a

def lcm( a, b ):
  return a*b/gcd( a, b )

for s in sys.stdin:
  d = map(int, s.split())
  a,b = d[0],d[1]
  print gcd(a,b),lcm(a,b)
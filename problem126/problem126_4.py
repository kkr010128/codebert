import sys
import numpy as np

def Ss():
  return sys.stdin.readline().rstrip().split(' ')

def Is():
  ss = Ss()
  return map(int, ss) if len(ss) > 1 else int(ss[0])

a, b, c, d, e = Is()
print(15 - a - b - c - d - e)
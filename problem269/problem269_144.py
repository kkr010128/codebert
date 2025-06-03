import sys
import math
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

T1, T2 = IL()
a1, a2 = IL()
b1, b2 = IL()
if a1*T1 + a2*T2 > b1*T1 + b2*T2:
  pass
else:
  a1,a2,b1,b2 = b1,b2,a1,a2

if a1*T1 + a2*T2 == b1*T1 + b2*T2:
  print("infinity")
elif a1*T1 >= b1*T1:
  print(0)
else:
  half = b1*T1 - a1*T1
  x = (a1*T1 + a2*T2 - (b1*T1 + b2*T2))
  # half/x >= n
  loop = half//x + 1
  if (loop - 1)*x == half:
    print(loop*2 -2)
  else:
    print(loop*2 -1)
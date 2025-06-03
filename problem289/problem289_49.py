import sys
input = sys.stdin.readline
import math
a,b,x = (int(i) for i in input().rstrip('\n').split())
if b*(a**2)<2*x:
  S=2*(b*(a**2)-x)
  res = math.atan2(S,a**3)
  res2 = math.degrees(res)
  print(res2)
else:
  res = math.atan2(2*x,a*(b**2))
  res2 = math.degrees(res)
  print(90-res2)
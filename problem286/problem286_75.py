import sys
a, b = map(int, sys.stdin.readline().split())
if a <= 9 and b <= 9:
  print(a*b)
else:
  print(-1)
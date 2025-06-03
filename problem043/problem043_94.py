import sys

for s in sys.stdin:
  a,b = sorted(map(int, s.split()))
  if a == 0 and b == 0:
    break
  print(a,b)
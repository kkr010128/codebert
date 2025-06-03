import sys
N, R = map(int, sys.stdin.readline().split())
if N < 10:
  print(R + (10-N)*100)
else:
  print(R)
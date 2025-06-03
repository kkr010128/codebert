import sys
K, X = map(int, sys.stdin.readline().strip().split())

if K * 500 >= X:
  print('Yes')
else:
  print('No')
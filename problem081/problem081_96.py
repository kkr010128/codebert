import sys

# A - Don't be late
D, T, S = map(int, input().split())

if S * T >= D:
  print('Yes')
else:
  print('No')
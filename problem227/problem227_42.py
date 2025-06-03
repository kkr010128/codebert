import sys

N, K = map(int, next(sys.stdin.buffer).split())
H = list(map(int, next(sys.stdin.buffer).split()))

if K:
  H.sort()
  print(sum(H[:-K]))
else:
  print(sum(H))

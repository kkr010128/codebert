import sys

for line in sys.stdin:
  H, W = map(int, line.split())

  if H == 0 and W == 0:
    break

  for _ in range(H):
    print( '#' * W )

  print("")
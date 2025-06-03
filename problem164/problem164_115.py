import sys

A, B, C, D = (int(x) for x in input().split())
while A>0 and C>0:
  C-=B
  if C<=0:
    print("Yes")
    sys.exit(0)
  A-=D
  if A<=0:
    print("No")
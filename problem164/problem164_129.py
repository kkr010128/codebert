a,b,c,d = list(map(int,input().split()))

while a > 0 or c > 0:
  c -= b
  if c <= 0:
    exit(print('Yes'))
  a -= d
  if a <= 0:
    exit(print('No'))

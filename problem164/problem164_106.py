a, b, c, d = map(int, input().split())

for i in range(max(a, b, c, d)):
  if b >= c:
    print('Yes')
    exit()
  else:
    c -= b
    if a <= d:
      print('No')
      exit()
    else:
      a -= d
      continue
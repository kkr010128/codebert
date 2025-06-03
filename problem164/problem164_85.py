A,B,C,D = (int(x) for x in input().split())
while True:
  C -= B
  if C <= 0:
    print('Yes')
    break
  else:
    A -= D
    if A <= 0:
      print('No')
      break
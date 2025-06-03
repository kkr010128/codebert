XY = [int(s) for s in input().split()]
X = XY[0]
Y = XY[1]

if Y % 2 == 0 and Y <= 4 * X and Y >= 2* X:
  print('Yes')
else:
  print('No')
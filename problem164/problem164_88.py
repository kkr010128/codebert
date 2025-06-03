a, b, c, d = [int(i) for i in input().split()]
if (a + d - 1) // d >= (c + b - 1) // b:
  print('Yes')
else:
  print('No')
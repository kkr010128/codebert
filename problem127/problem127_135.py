x, y = list(map(int, input().split()))
a = 4 * x - y
b = y - 2 * x
if (a % 2 == 0 and a >= 0) and (b % 2 == 0 and b >= 0):
  print('Yes')
else:
  print('No')
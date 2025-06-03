a, b = list(map(int, input().split()))
if b % 2 == 0 and 2 * a <= b <= 4 * a:
  print('Yes')
else:
  print('No')
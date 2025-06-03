a, b, c = map(int, input().split())
x = c-a-b
if x <= 0:
  print('No')
elif 4*a*b < x*x:
  print('Yes')
else:
  print('No')
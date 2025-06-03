X, Y = map(int, input().split())

x = 2*X-1/2*Y
y = -X + 1/2*Y

if x.is_integer() and y.is_integer() == True:
  if x >= 0 and y >= 0:
    print('Yes')
  else:
    print('No')
else:
  print('No')
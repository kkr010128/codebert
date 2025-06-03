xy = [int(s) for s in input().split()]
x = xy[0]
y = xy[1]

if y % 2 == 0 and y<=4*x and y>=2*x:
  print('Yes')
else:
  print('No')
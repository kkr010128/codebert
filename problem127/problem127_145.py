x,y=map(int,input().split())
if y%2==1:
  print('No')
elif y>=2*x and y<=4*x:
  print('Yes')
else:
  print('No')
x,y=map(int,input().split())
if y%2 == 1:
  print('No')
elif x*2 > y:
  print('No')
elif x*4 < y:
  print('No')
else:
  print('Yes')
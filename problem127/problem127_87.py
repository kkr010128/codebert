X,Y = map(int, input().split())

if X * 2 > Y:
  print('No')
elif X * 4 < Y:
  print('No')
else:
  for i in range(0,X+1):
    if Y == (X * 2) + (i * 2):
      print('Yes')
      break
  else:
    print('No')
      


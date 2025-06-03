while True:
 (x,y) = [int(i) for i in input().rstrip().split(' ')]
 if x == y  == 0:
  break
 if(x < y):
  print('{0} {1}'.format(x,y))
 else:
  print('{0} {1}'.format(y,x))
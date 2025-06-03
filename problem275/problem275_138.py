x,y = map(int,input().split())
def point(a):
  if a == 1:
    return 300000
  elif a == 2:
    return 200000
  elif a == 3:
    return 100000
  else:
    return 0
  
c = point(x)
b = point(y)

if x == 1 and y == 1:
  print(1000000)
else:
  print(c+b)
x, y = map(int, input().split())
def shokin(z):
  if z == 1:
    return 300000
  elif z == 2:
    return 200000
  elif z == 3:
    return 100000
  else:
    return 0
v = 0
if x == 1 and y == 1:
  v = 400000
  
print(shokin(x)+shokin(y)+v)
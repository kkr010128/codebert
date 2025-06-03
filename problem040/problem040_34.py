x,y,z=map(int, input().split())
if x<=y<=z:
  print(x,y,z)
elif x<=z<=y:
  print(x,z,y)
elif y<=z<=x:
  print(y,z,x)
elif y<=x<=z:
  print(y,x,z)
elif z<=x<=y:
  print(z,x,y)
else:
  print(z,y,x)

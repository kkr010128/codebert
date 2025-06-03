x, y = map(int,input().split())
if (y%2 == 1):
  print("No")
else:
  if (y < x*2):
    print("No")
  elif (y > x*4):
    print("No")
  else:
    print("Yes")
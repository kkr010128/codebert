x, y = map(int,input().split())
min = 2 * x
gap = y - min

if gap < 0 or gap > min:
  print("No")
else:
  if gap % 2 == 0:
    print("Yes")
  else:
    print("No")

whxyr = input().split()
[w, h, x, y, r] = [int(x) for x in whxyr]
if 0 <= x - r and x + r <= w and 0 <= y - r and y + r <= h:
  print("Yes")
else:
  print("No")
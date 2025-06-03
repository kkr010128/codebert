x, y = map(int, input().split())
if y in range(x*2, x*4+1, 2):
  print("Yes")
else:
  print("No")
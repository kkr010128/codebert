x = int(input())
if x >= 2000:
  print(1)
else:
  d = 0
  for i in range(1,20):
    if 100*i <= x <= 105*i:
      print(1)
      d += 1
      break
  if d == 0:
    print(0)
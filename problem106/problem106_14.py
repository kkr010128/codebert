nn=int(input())
nc = [0] * (nn + 1)
for x in range(1, 100):
  for y in range(1, 100):
    for z in range(1, 100):
      a = x * x + y * y + z * z + x * y + x * z + y * z
      if a > nn:
        break
      nc[a] += 1
for i in range(1, nn + 1):
  print(nc[i])
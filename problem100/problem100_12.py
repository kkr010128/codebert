x = int(input())
j = 8
for low in range(400, 2000, 200):
  if low <= x < low + 200:
    print(j)
    break
  j -= 1
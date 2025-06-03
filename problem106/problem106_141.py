n = int(input())
lst = [0] * 10**6
for x in range(1, 101):
  for y in range(1, 101):
    for z in range(1, 101):
      t = (x**2 + y**2 + z**2 + (x+y+z)**2) // 2
      lst[t] += 1
for i in range(1, n+1):
  print(lst[i])
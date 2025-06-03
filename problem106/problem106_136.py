n = int(input())

count = [0 for i in range(n+1)]

for x in range(1, 101):
  for y in range(1, 101):
    for z in range(1, 101):
      f = x ** 2 + y ** 2 + z ** 2 + x*y + y*z + z*x
      if f <= n:
        count[f] += 1

for i in count[1:]:
  print(i)
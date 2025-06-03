n = int(input())

ans = [0 for _ in range(10001)]
for x in range(1, 100):
  for y in range(1, 100):
    for z in range(1, 100):
      v = x**2 + y**2 + z**2 + x*y + y*z + z*x
      if v < 10001:
        ans[v] += 1

for i in range(n):
  print(ans[i+1])
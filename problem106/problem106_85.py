N = int(input())
ans = [0 for _ in range(N + 1)]

for x in range(1, 101):
  for y in range(1, 101):
    for z in range(1, 101):
      v = x * x + y * y + z * z  + x * y + y * z + z * x
      if v > N:
        continue
      ans[v - 1] += 1

for i in range(N):
  print(ans[i])
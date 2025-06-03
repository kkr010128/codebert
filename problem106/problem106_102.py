N = int(input())
L = [0] * N
for x in range(1,101):
  for y in range(1,101):
    for z in range(1,101):
      n = int(((x + y) ** 2 + (y + z) ** 2 + (z + x) ** 2)/ 2 )
      if n <= N:
        L[n - 1] += 1
print(*L, sep='\n')

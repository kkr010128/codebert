n = int(input().rstrip())

ans = [0 for x in range(10000)]
for x in range(1,101):
  for y in range(1,101):
    for z in range(1,101):
      f = ((x+y)**2 + (y+z)**2 + (z+x)**2)//2
      if f <= 10000:
        ans[f-1] += 1

for i in range(n):
  print(ans[i])
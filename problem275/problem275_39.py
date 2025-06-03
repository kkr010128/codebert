x = list(map(int, input().split()))
top_count = 0
ans = 0
for i in x:
  if i == 1:
    ans += 300000
    top_count += 1

  elif i == 2:
    ans += 200000

  elif i == 3:
    ans += 100000

if top_count == 2:
  print(ans + 400000)
else:
  print(ans)
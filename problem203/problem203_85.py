a, b = map(int, input().split())

ans = 1001
for n in range(1001):
  if n * 8 // 100 == a and n * 10 // 100 == b:
    ans = min(ans, n)

if ans < 1001:
  print(ans)
else:
  print(-1)
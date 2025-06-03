n, a, b = map(int, input().split())
ans = 0
if (a - b) % 2 == 0:
  ans = (b - a)// 2
else:
  ans = min(a + (b - a - 1) // 2, n - b + (b - a + 1) // 2)
print(ans)
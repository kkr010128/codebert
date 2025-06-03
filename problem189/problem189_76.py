n, m = map(int, input().split())
ans = 0
for i in range(1, n):
  ans += i
for i in range(1, m):
  ans += i
print(ans)
n = int(input())
a = list(map(int, input().split()))

t = 1
ans = 0
for i in range(n):
  if t != a[i]:
    ans += 1
    a[i] = -1
  else:
    t += 1

if all([i == -1 for i in a]):
  print(-1)
else:
  print(ans)
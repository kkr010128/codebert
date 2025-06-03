n, m = map(int, input().split())
S = list(map(int, input()))[::-1]
L = []
now = 0
while now < n:
  if n - now <= m:
    L.append(n - now)
    break
  for i in range(m, 0, -1):
    if not S[now+i]:
      now += i
      L.append(i)
      break
  else:
    print(-1)
    exit()
print(*L[::-1])
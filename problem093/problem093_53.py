N,K = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = -1* 10**9

for si in range(N):
  s = list()
  total = 0
  l = 0
  x = si
  while(1):
    x = p[x] - 1
    s.append(c[x])
    total += c[x]
    l += 1
    if x == si:
      break
  t = 0
  for j in range(l):
    t += s[j]
    now = t
    if j >= K:
      break
    if total > 0:
      e = (K-j-1)//l
      now += total * e
    ans = max(ans, now)

print(ans)
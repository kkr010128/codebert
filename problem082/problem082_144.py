s = input()
t = input()
n = len(s)
m = len(t)
ans = 2000
for i in range(n):
  if i+m > n:
    break
  u = s[i:i+m]
  cnt = 0
  for j in range(m):
    if t[j] != u[j]:
      cnt += 1
  ans = min(ans, cnt)
print(ans)
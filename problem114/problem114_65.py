D = int(input())
c = list(map(int, input().split()))
s = [[]]
for _ in range(D):
  s.append(list(map(int, input().split())))

lasts = [0 for i in range(len(c))]
ans = 0
for d in range(1, D+1):
  t = int(input()) - 1
  lasts[t] = d
  ans += s[d][t]
  for i in range(len(c)):
    ans -= c[i] * (d - lasts[i])
  print(ans)
n = int(input())
a = list(map(int, input().split()))

ans = 0
t = 1
s = []
for i in a:
  if i != t: ans += 1
  else:
    t += 1
    s.append(i)

if s == []:
  print(-1)
else:
  print(ans)
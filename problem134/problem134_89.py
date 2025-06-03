n = int(input())
l = list(map(int, input().split()))
l.sort()
c = 1
i = 0
while i < n:
  c *= l[i]
  i += 1
  if c > 1000000000000000000:
    break
if c <= 1000000000000000000:
  print(c)
else:
  print(-1)
n, m = map(int, input().split())
a = sorted(map(int, input().split()), reverse = True)
total = sum(a)
cnt = 0
for i in a:
  if i * 4 * m >= total:
    cnt += 1
  else:
    break
if cnt >= m:
  print("Yes")
else:
  print("No")
N = int(input())
A = list(map(int, input().split()))

cnt = 0
now = 0
for a in A:
  if a == now + 1:
    now += 1
  else:
    cnt += 1

if now == 0:
  print(-1)
else:
  print(cnt)

N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
sumA = sum(A)
for a in A:
  if a >=  sumA / 4 / M:
    cnt += 1
if cnt >= M:
  print('Yes')
else:
  print('No')

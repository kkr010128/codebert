N, M, X = map(int,input().split())
CA = list(list(map(int,input().split())) for _ in range(N))

cost = (10 ** 5) * 12

for i in range(2 ** N):
  total, a = 0, [0] * M
  for j in range(N):
    if i >> j & 1:
      total += CA[j][0]
      for k in range(M): a[k] += CA[j][k + 1]
  for j in range(M):
    if a[j] < X:
      if i == 2 ** N - 1: cost = -1
      break
  else: cost = min(cost, total)

print(cost)
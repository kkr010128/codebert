N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]

sum_money = float("inf")
for i in range(2 ** N):
  money = 0
  algorithm = [0]*M
  for j in range(N):
    if (i >> j) & 1 == 1:
      money += CA[j][0]
      for k in range(M):
        algorithm[k] += CA[j][k+1]
  check = True
  for l in algorithm:
    if l < X:
      check = False
  if check:
    sum_money = min(sum_money, money)
    
print(sum_money if sum_money != float("inf") else -1)
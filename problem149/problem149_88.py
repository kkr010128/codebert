N, M, X = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(N)]
answer = 10**7

for num in range(2**N):
  algos = [0 for i in range(M+1)]
  money = 0
  for i in range(N):
    if num>>i&1:
      for j in range(1, M+1):
        algos[j] += books[i][j]
      money += books[i][0]
  master = True
  for k in range(1, M+1):
    if algos[k] < X:
        master = False
        break
  if master:
    answer = min(answer, money)
if answer == 10**7:
  print(-1)
else:
  print(answer)
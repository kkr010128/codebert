N = int(input())
stocks = list(map(int, input().split()))
curr = 1000
for i in range(N - 1):
  cnt = 0
  if stocks[i] < stocks[i + 1]:
    cnt = curr // stocks[i]
  curr += cnt * (stocks[i + 1] - stocks[i])
print(curr)

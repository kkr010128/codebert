n, m, x = map(int, input().split())

price = []
ability = []
for _ in range(n):
  lst = []
  lst = [int(i) for i in input().split()]
  price.append(lst[0])
  ability.append(lst[1:m + 1])
#print(price)
#print(ability)
min_price = float('inf')
for i in range(2 ** n):
  flag = True
  total = 0
  obtain = [0] * m
  for j in range(n):
    if ((i >> j) & 1):
      total += price[j]
      for k in range(m):
        obtain[k] += ability[j][k]
  for j in range(m):
    if obtain[j] < x:
      flag = False
      break
  if flag:
    if total < min_price:
      min_price = total
if min_price == float('inf'):
  print(-1)
else:
  print(min_price)
import itertools

n, m, x = map(int, input().split())
A = []
for _ in range(n):
  A.append(list(map(int, input().split())))

c = [ (0, 1) for _ in range(n)]
min_price = float('inf')

for cc in itertools.product(*c):
  xx = [0] * m
  price = 0
  for i, ccc in enumerate(cc):
    if ccc==1:
      price += A[i][0]
      xx = [a +b for a, b in zip(xx, A[i][1:])]
  if min(xx) >= x:
    min_price = min(min_price, price)

if min_price==float('inf'):
  print(-1)
else:
  print(min_price)
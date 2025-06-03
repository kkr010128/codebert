A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
price_list = []

for i in range(M):
  x, y, c = map(int, input().split())
  price = a[x-1] + b[y-1] - c
  price_list.append(price)


a.sort()
b.sort()
price_list.append(a[0]+b[0])
min_price = price_list[0]

for n in price_list:
  if min_price >= n:
    min_price = n
  elif min_price < n:
    pass


print(min_price)
n = int(input())
a = list(map(int, input().split()))
a = a + [0]
state = a[0]
money = 1000
stock = 0
for i in range(1, n+1):
  if state < a[i] and stock == 0:
    stock += (money // state)
    money %= state
  elif state > a[i] and stock > 0:
    money += (stock * state)
    stock = 0
  state = a[i]
print(money)

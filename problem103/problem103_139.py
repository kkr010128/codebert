n = int(input())
tmp = input().split(' ')
tmp_map = map(int,tmp)
prices = list(tmp_map)
money = 1000

for i in range(n-1):
  if prices[i] < prices[i+1]:
    stocks = int(money/prices[i])
    money += stocks*(prices[i+1]-prices[i])

print(money)
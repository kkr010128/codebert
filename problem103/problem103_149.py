days = int(input())
price = list(map(int,input().split()))
money = 1000
stock = 0

for i in range(days - 1):
  if price[i] < price[i + 1]:
    new = (money // price[i])
    stock += new
    money -= (new * price[i])
    
  else:
    money += stock * price[i]
    stock = 0

print(money + stock * price[-1])
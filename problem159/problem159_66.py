x = int(input())
money = 100
year = 0

while True:
  money = money + money*100//10000
  year += 1

  if money >= x:
    print(year)
    exit()
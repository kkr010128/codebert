x = int(input())
money = 100
year = 0
if x <= 100:
  print(0)
  exit()
while True:
  money += money*100//10000
  year += 1

  if money >= x:
    print(year)
    exit()
import math
x=int(input());money=100;year=0
while True:
  if money >= x:
    print(year)
    break
  money+=money//100
  year+=1
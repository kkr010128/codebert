money = int(input())
if money%1000==0:
  print(0)
else:
  print(1000-(money % 1000))
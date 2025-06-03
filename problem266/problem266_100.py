X = int(input())

num = X//100
amari = X%100

if num*5 >= amari:
  print(1)
else:
  print(0)
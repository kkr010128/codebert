pay = int(input())
if pay % 1000 == 0:
  print(0)
else:
  print(1000 - pay % 1000)
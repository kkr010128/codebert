price = int(input())
amari = price % 1000
if amari == 0:
  print(0)
else:
  print(1000 - amari)
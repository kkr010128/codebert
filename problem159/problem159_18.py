from decimal import Decimal

x = int(input())

t = 100
n = 0
while t < x:
  t += t // 100
  n += 1
print(n)
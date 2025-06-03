import math

X = int(input())
year = 0
amount = 100
while True:
  if amount >= X:
    break
  amount += math.floor(amount//100)
  year += 1
print(year)
import math

weeks = int(input())
money = 100

for i in range(0, weeks):
    money = math.ceil(money * 1.05)

print(money * 1000)
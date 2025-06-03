import math

n = input()
money = 100000

for i in range(0, n):
    money = money*1.05
    money /= 1000
    money = int(math.ceil(money)*1000)

print money
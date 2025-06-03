import math
n = input()
p = 0
money = 100
while p != n:
    money = math.ceil(money * 1.05)
    p += 1
print int(money * 1000)
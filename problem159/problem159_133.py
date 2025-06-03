import math
x = int(input())
money = 100
count = 0
while money <= x:
    if x == money:
        break
    money = money + money // 100
    count += 1
print(count)
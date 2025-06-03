from decimal import Decimal

x = int(input())
money = 100
ans = 0

while 1:
    ans += 1
    money = money + int(money * Decimal(str(0.01)))
    if money >= x:
        print(ans)
        exit()
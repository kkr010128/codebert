x, y = map(int, input().split())
money = [300000, 200000, 100000]
if x == 1 and y == 1:
    print(1000000)
elif x <= 3 and y <= 3:
    print(money[x - 1] + money[y - 1])
elif x <= 3:
    print(money[x - 1])
elif y <= 3:
    print(money[y - 1])
else:
    print(0)
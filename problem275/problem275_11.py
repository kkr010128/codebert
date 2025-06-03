x, y = map(int, input().split())

total_money = 0

if x >= 4:
    total_money += 0
elif x == 3:
    total_money += 100000
elif x == 2:
    total_money += 200000
elif x == 1:
    total_money += 300000

if y >= 4:
    total_money += 0
elif y == 3:
    total_money += 100000
elif y == 2:
    total_money += 200000
elif y == 1:
    total_money += 300000

if x == 1 and y == 1:
    total_money += 400000

print(total_money)

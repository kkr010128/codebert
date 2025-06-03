money = 100000
for _ in range(int(input())):
    money += int(money * 0.05)
    if money % 1000 != 0:
        while money % 1000 != 0:
            money += 1
print(money)
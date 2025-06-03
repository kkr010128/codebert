N = input()
money = 100000
for i in range(N):
    money = int(money *1.05)
    if money % 1000 != 0:
        money = (money // 1000 + 1) * 1000
print money
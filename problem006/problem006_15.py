n = input()
money = 100000
for i in range(n):
    money = int(money * 1.05)
    if money != money / 1000 * 1000:
        money = money / 1000 * 1000 + 1000
print money
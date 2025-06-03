X = int(input())
money = 100
ans = 0

while money < X:
    tax = money // 100
    money += tax
    ans += 1

print(ans)
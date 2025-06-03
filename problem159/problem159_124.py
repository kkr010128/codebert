x = int(input())
money = 100
k = 1

cnt = 0

while money < x:
    money += k
    k = money // 100
    cnt += 1

print(cnt)
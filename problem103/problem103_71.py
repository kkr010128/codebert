n = int(input())
data = list(map(int, input().split()))

ans = 0
money = 1000

for idx in range(n-1):
    today = data[idx]
    tmr = data[idx+1]
    if tmr > today:
        money += (tmr-today) * (money//today)

print(money)
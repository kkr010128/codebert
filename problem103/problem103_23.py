N = int(input())
A = list(map(int, input().split()))

money = 1000
stock = 0
for day in range(N-1):
    today_price = A[day]
    tommorow_price = A[day+1]
    if today_price < tommorow_price:
        div,mod = divmod(money, today_price)
        stock += div
        money = mod
    elif today_price > tommorow_price:
        money += today_price * stock
        stock = 0
money += A[N-1] * stock
print(money)
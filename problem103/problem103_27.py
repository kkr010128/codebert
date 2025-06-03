n = int(input())
A = [0] + [*map(int, input().split())]
dp_stock = [0]*(n+1)
dp_yen = [0]*(n+1)
dp_yen[0] = 1000
for day in range(1, n+1):
    dp_stock[day] = max(dp_stock[day-1], dp_yen[day-1] // A[day])
    remain = dp_yen[day-1] - dp_stock[day-1]*A[day-1]
    dp_yen[day] = max(dp_yen[day-1], remain + dp_stock[day-1] * A[day])
print(dp_yen[n])

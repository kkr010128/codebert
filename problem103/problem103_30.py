n = int(input())
A = [*map(int, input().split())] + [0]
dp_yen = [0]*(n+1)
dp_yen[0] = 1000
for day in range(n):
    dp_yen[day+1] = max(dp_yen[day], dp_yen[day] + (A[day+1] - A[day]) * (dp_yen[day] // A[day]))
print(dp_yen[n])

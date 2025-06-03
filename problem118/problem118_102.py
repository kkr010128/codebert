N = int(input())
tot = 0
for i in range(1, N+1):
    m = N//i
    tot += i * (m * (m+1)) // 2
print(tot)
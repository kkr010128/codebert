n = int(input())

ans = 0

for i in range(1, n + 1):
    t = n//i
    ans += 0.5 * i * t * ( t + 1)

print(int(ans))
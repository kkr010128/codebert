n = int(input())
ans = 0
for m in range(1, int(n**.5) + 1):
    ans += m * (m + (n // m)) * ((n // m) + 1 - m)
k = int(n**.5)
ans -= k * (k + 1) * (2 * k + 1) // 6

print(ans)
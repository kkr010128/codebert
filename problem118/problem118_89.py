n = int(input())
ans = (n + 1) * n // 2
for i in range(2, n + 1):
    j = 1
    while i * j <= n:
        ans += i * j
        j += 1
print(ans)

n = int(input())

ans = 0
for i in range(1, n+1):
    g = n // i
    ans += i * (g*(g+1))//2

print(ans)

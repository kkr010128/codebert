n, k = map(int, input().split())
ans = 0
for i in range(k, n + 2):
    l = int(i * (i - 1) / 2)
    r = n * i - l
    ans += r - l + 1
    ans %= 10 ** 9 + 7
print(ans)
N = int(input())
ans = 0
for i in range(1, N + 1):
    n = N // i  # 項数n
    cnt = (n * (2 * i + (n - 1) * i)) // 2  # 初項i, 項数n の等差数列の和の公式
    ans += cnt
print(ans)
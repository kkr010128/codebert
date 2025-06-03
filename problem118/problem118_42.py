N = int(input())
ans = 0

for i in range(1, N + 1):
    # 初項
    a0 = i
    # 公差
    d = i
    # 項数
    n = N // i

    temp = int(0.5 * n * (2 * a0 + (n - 1) * d))
    ans += temp

print(ans)

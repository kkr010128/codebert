n, a, b = map(int, input().split())
ans = 0
if (b - a) % 2 == 0:
    ans = (b - a) // 2
else:
    # ans += (b - a) // 2
    # a += ans
    # b -= ans
    # ans += min(n - a, b - 1)
    if a - 1 <= n - b:
        ans += a
        b -= a
        a = 1
    else:
        ans += n - b + 1
        a += n - b + 1
        b = n
    ans += (b - a) // 2
print(ans)
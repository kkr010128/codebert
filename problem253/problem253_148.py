n, a, b = map(int, input().split())
# 偶奇一致
if a % 2 == b % 2:
    print((b - a) // 2)
else:
    left = a - 1
    right = n - b

    if left > right:
        cnt = right + 1
        left = min(a + cnt, n)
        print((n - left) // 2 + cnt)
    else:
        cnt = left + 1
        right = max(b - cnt, 1)
        print((right - 1) // 2 + cnt)

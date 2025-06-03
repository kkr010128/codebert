while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break
    cnt = 0
    upper_max_value = min(x - 3, n)
    lower_max_value = max(int(x / 3), 3)
    for i in range(upper_max_value, lower_max_value - 1, -1):
        for j in range(i - 1, 1, -1):
            for k in range(j - 1, 0, -1):
                if (i + j + k) == x:
                    cnt += 1
    print(cnt)
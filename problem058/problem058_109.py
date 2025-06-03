while True:
    n, x = map(int, raw_input().split())
    if n == x == 0:
        break;
    cnt = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            tmp = x - i - j
            if tmp > j and tmp <= n:
                cnt += 1
    print cnt
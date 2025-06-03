while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break

    c = 0
    for i in range(1, int(x/3)+2):
        for j in range(i+1, int(x/2)+2):
            k = x - i - j
            if k <= j:
                break
            elif k <= n:
                c += 1
    print(c)
while True:
    c = input().split()
    n, x = int(c[0]), int(c[1])
    if n == x == 0:
        break
    count = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if i + j + k == x:
                    count += 1
    print(count)


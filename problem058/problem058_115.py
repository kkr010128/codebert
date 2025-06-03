while True:
    c = 0
    n, x= map(int, input().split())
    if n == 0 and x == 0:
        break
    for i in range(1, n + 1):
        for j in range(1, n + 1 ):
            if j <= i:
                continue
            for k in range(1, n + 1):
                if k <= j:
                    continue
                if i != j and i != k and j != k and i + j + k == x:
                    c += 1
    print(c)

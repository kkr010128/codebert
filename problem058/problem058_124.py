while True:
    (n, x) = [int(i) for i in input().split()]
    if n == x == 0:
        break

    count = 0
    for a in range(1, n + 1):
        if a >= x:
            break
        for b in range(a + 1, n + 1):
            if sum([a,b]) >= x:
                break
            for c in range(b + 1, n + 1):
                if sum([a,b,c]) == x:
                    count += 1

    print(count)
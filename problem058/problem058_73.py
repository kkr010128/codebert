while True:
    (n, x) = [int(i) for i in input().split()]
    if n == x == 0:
        break

    count = 0
    start = n if n < x else x
    for a in range(start, 0, -1):
        if a >= x:
            continue
        for b in range(a - 1, 0, -1):
            if sum([a,b]) >= x:
                continue
            for c in range(b - 1, 0, -1):
                if sum([a,b,c]) == x:
                    count += 1
    print(count)
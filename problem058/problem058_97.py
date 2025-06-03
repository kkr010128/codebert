while True:
    n, x = map(int, input().split())
    if n == 0:
        break

    count = 0
    for n1 in range(1, n+1):
        for n2 in range(n1+1, n+1):
            for n3 in range(n2+1, n+1):
                if n1 + n2 + n3 == x:
                    count += 1

    print(count)
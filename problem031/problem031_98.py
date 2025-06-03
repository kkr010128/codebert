while True:
    n = int(input())

    if n == 0:
        break

    si = list(map(int, input().split()))
    m = sum(si) / n
    func = (lambda x: (x - m) ** 2)
    print((sum(map(func, si)) / n) ** .5)


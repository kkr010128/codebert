while True:
    n = int(input())
    if n == 0:
        break

    s = list(map(int, input().split()))
    kei = 0
    for p in s:
        kei += p

    m = kei / n

    a = 0
    for p in s:
        a += ((p - m)**2) / n

    import math
    h = math.sqrt(a)
    print(h)
while True:
    n = int(input())
    if n == 0:
        break

    s = list(map(float, input().split()))
    m = sum(s) / n

    v = sum([(x - m) ** 2 for x in s]) / n
    print(v ** 0.5)
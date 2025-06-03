def counter(a, b, c):
    count = 0
    for n in range(a, b+1):
        if c % n == 0:
            count += 1
    print(count)

a, b, c = list(map(int, input().split()))
counter(a, b, c)
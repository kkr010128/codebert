x, n = map(int, input().split())
p = list(map(int, input().split()))
if x not in p:
    print(x)
else:
    a, b = 1, 1
    while True:
        if (x + a) not in p:
            break
        else:
            a += 1

    while True:
        if (x - b) not in p:
            break
        else:
            b += 1

    if a >= b:
        print(x - b)
    else:
        print(x + a)
while True:
    (x, y) = [int(i) for i in input().split()]

    if x < y:
        print(x, y)
    elif x > y:
        print(y, x)
    elif x == y:
        if x == 0 and 0 == y:
            break
        print(x, y)
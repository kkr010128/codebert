while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    else:
        a = [x, y]
        a.sort()
        print(a[0], a[1])
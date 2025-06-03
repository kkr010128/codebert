h,w = [],[]
while True:
    (h,w) = [int(x) for x in input().split()]
    if h == w == 0:
        break
    for x in range(h):
        for y in range(w):
            if (x + y) % 2 == 0:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()
while True:
    h, w = map(int, input().split())

    if h == 0 and w == 0:
        break

    for y in range(h):
        isOddLine = True
        if y % 2 == 0:
            isOddLine = False
        else:
            isOddLine = True

        for x in range(w):
            if isOddLine:
                if x % 2 == 0:
                    print('.', end='')
                else:
                    print('#', end='')
            else:
                if x % 2 == 0:
                    print('#', end='')
                else:
                    print('.', end='')
        print('')
    print('')
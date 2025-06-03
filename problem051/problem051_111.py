while True:
    h, w = map(int, input().split())

    if h == 0 and w == 0:
        break

    width = ''

    for i in range(h):
        if i % 2 == 0:
            for j in range(w):
                if j % 2 == 0:
                    width += '#'
                else:
                    width += '.'
        else:
            for j in range(w):
                if j % 2 != 0:
                    width += '#'
                else:
                    width += '.'
        print(width)
        width = ''

    print('')

while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    width = ''
    for j in range(h):
        if j == 0 or j == h - 1:
            for i in range(w):
                width += '#'
        else:
            for i in range(w):
                if i == 0 or i == w - 1:
                    width += '#'
                else:
                    width += '.'
        print(width)
        width = ''
    print('')

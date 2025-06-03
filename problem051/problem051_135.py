while(True):
    h, w = map(int, input().split())
    if(h == 0 and w == 0):
        break
    for i in range(h):
        s = ''
        for j in range(w):
            if (i + j) % 2 == 0:
                s += '#'
            else:
                s += '.'
        print(s)
    print()


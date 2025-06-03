while True:
    h, w = map(int, input().split())
    if(w == h == 0): break
    for i in range(h):
        for j in range(w):
            if (i + j) % 2:
                print('.', end = '')
            else:
                print('#', end = '')
        print('')
    print('')


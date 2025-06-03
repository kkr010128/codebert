H, W = map(int, raw_input().split())
while H | W != 0:
    for i in range(H):
        s = ''
        for j in range(W):
            s += '#' if (j + i) % 2 == 0 else '.'
        print s
    print ''
    H, W = map(int, raw_input().split())
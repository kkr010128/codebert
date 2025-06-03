while True:
    h, w = map(int, input().split())
    if h == w == 0: break
    for c in ['\n' if y == w else '#' if (x+y) % 2 == 0 else '.' for x in range(0,h) for y in range(0, w + 1)]: print(c, end='')
    print('')
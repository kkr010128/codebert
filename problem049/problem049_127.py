while True:
    h, w = map(int, input().split())
    if h == w == 0: break
    for i in range(0, h):
        print(''.join(['#' for x in range(0, w)]))
    print('')
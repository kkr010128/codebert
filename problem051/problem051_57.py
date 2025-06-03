while True:
    H,W = map(int,input().split())
    if H == W == 0:
        break
    a = '#.'
    b = '#'
    c = '.#'
    d = '.'

    def bw(n):
        if n % 2 == 0:
            print((n//2)*a)
        else:
            print((n//2)*a + b)

    def wb(n):
        if n % 2 == 0:
            print((n//2)*c)
        else:
            print((n//2)*c + d)

    for i in range(1,H + 1):
        if i % 2 == 0:
            wb(W)
        else:
            bw(W)
    print()
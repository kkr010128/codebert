def rect(h, w):
    a = '#.' * 150
    b = '.#' * 150
    while h > 0:
        print(a[:w])
        a, b = b, a
        h -= 1
    print()
    return

while True:
    n = list(map(int, input().split()))
    H = n[0]
    W = n[1]
    if (H == 0 and W == 0):
        break
    rect(H, W)
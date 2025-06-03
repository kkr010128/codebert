while True:
    H, W = [int(x) for x in input().split()]
    if H == W == 0:
        break
    for i in range(H):
        if i == 0 or i == H - 1:
            print('#'*W)
        else:
            print(''.join(['#' if c == 0 or c == W - 1 else '.' for c in range(W)]))
    print()
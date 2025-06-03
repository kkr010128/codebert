while True:
    (H,W) = [int(x) for x in input().split()]
    if H == W == 0:
        break

    for hc in range(H):
        if hc == 0 or hc == H - 1:
            print('#'* W)
        else:
            print('#' + '.' * (W - 2) + '#')
    print()    
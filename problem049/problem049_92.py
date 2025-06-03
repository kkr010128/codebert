while True:
    H, W = list(map(int, input().split()))
    if H == 0 and W == 0:
        break

    for h in range(H):
        for w in range(W):
            if w == (W - 1):
                print('#')
                break
            print('#', end="")
    print()

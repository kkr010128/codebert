while True:
    H, W = [int(x) for x in input().split()]
    if H == W == 0:
        break
    for i in range(H):
        cnt = i % 2
        for j in range(W):
            if (cnt % 2) == 0:
                print('#', end="")
            else:
                print('.', end="")
            cnt += 1
        print()
    print()
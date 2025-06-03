H = 1
W = 1
while H and W:
    H, W = input().split()
    H = int(H)
    W = int(W)
    if H == 0\
    and W == 0:
        break

    for h in range(H):
        for w in range(W):
            if h % 2 and w % 2\
            or h % 2 == 0 and w % 2 == 0:
                print("#", end = "")
            else:
                print(".", end = "")

            if w == W - 1:
                print()
    print()
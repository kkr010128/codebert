while True:
    (H, W) = [int(x) for x in input().split()]

    if H == W == 0:
        break

    for row in range(H):
        if row % 2 == 0:
            for w in range(W):
                if w % 2 == 0:
                    print("#", end="")
                else:
                    print(".", end="")

            else:
                print()
        else:
            for w in range(W):
                if w % 2 == 0:
                    print(".",end="")
                else:
                    print("#",end="")

            print()
    print()
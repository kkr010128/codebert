while True:
    H, W = map(int, input().split())
    if (H == W == 0):
        break
    else:
        for j in range(H):
            if (j == 0 or j == H - 1):
                for i in range(W):
                    print("#", end='')
            else:
                for f in range(W):
                    if (f == 0 or f == W - 1):
                        print("#", end='')
                    else:
                        print(".", end='')


            print()
        print()
while True:
    H, W = map(int, input().split())
    if (H == W == 0):
        break
    else:
        for j in range(H):
            if (j % 2 == 0):
                for i in range(W):
                    if(i % 2 == 0):
                        print("#", end='')
                    else:
                        print(".", end='')
            else:
                for f in range(W):
                    if(f % 2 == 0):
                        print(".", end='')
                    else:
                        print("#", end='')


            print()
        print()
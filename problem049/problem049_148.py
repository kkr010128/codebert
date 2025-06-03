while(True):
    H, W = map(int, input().split())
    if(H == W == 0):
        break
    first = False
    for i in range(H):
        print("#" * W)
    print()
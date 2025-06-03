while 1:
    H, W = map(int, input().split())
    if H ==0 and W == 0:
        break
    for i in range(H):
        for j in range(W):
            if (j % 2 == 0 and i % 2 == 0)\
            or (j % 2 != 0 and i % 2 != 0): 
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()
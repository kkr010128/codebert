while True:
    H, W = [int(x) for x in input().split() if x.isdigit()]
    if H ==0 and W == 0:
        break
    else:
        for i in range(H):
            for j in range(W-1):
                print("#", end='')
            print("#")
        print("")
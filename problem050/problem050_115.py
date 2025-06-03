while True:
    H, W = [int(x) for x in input().split() if x.isdigit()]
    if H ==0 and W == 0:
        break
    else:
        for i in range(H):
            print("#", end='')
            if i == 0 or i == H-1:
                for j in range(W-2):
                    print("#", end='')
            else:
                for j in range(W-2):
                    print(".", end='')
            print("#")
        print("")
while(True):
    (H,W)=[int(s) for s in input().split()]
    if (H,W) == (0,0):
        break
    for j in range(H):
        print("#"*W)
    print("")
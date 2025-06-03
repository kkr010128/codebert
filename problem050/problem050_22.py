while True:
    H,W = map(int,raw_input().split())
    if (H,W) == (0,0):
        break
    for k in range(H):
        if k==0 or k==H-1:
            print "#"*W
        else:
            print "#" + "." * (W-2) + "#"
    print ""
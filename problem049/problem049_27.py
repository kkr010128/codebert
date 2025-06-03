while True:
    s = input().split(" ")
    H = int(s[0])
    W = int(s[1])
    if H == 0 and W == 0:
        break
    for i in range(H):
        for j in range(W):
            if j == W-1:
                print("#")
            else:
                print("#",end="")
    print("")
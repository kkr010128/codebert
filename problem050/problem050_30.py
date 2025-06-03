while True:
    s = input().split(" ")
    H = int(s[0])
    W = int(s[1])
    if H == 0 and W == 0:
        break
    for i in range(H):
        for j in range(W):
            if i == 0 or i == H-1:
                print("#",end="")
            else:
                if j == 0 or j == W-1:
                    print("#",end="")
                else:
                    print(".",end="")
        print("")
    print("")
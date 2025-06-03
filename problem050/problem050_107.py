while True:
    H,W = [int(i) for i in input().split()]
    if H == 0 and W == 0:
        break
    else:
        for line in list(range(1,H+1,1)):
            for column in list(range(1,W+1,1)):
                if line == 1 or line == H:
                    if column == W:
                        print("#")
                    else:
                        print("#", end = "")

                else:
                    if column == 1:
                        print("#", end = "")
                    elif column == W:
                        print("#")
                    else:
                        print(".", end = "")
        print("")

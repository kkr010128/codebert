while True:
    H,W = [int(i) for i in input().split()]
    if H == 0 and W == 0:
        break
    else:
        for line in list(range(1,H+1,1)):
            for column in list(range(1,W+1,1)):
                if line%2 == 1:
                    if column%2 == 1:
                        if column == W:
                            print("#")
                        else:
                            print("#", end = "")
                    else:
                        if column == W:
                            print(".")
                        else:
                            print(".", end = "")

                else:
                    if column%2 == 1:
                        if column == W:
                            print(".")
                        else:
                            print(".", end = "")
                    else:
                        if column == W:
                            print("#")
                        else:
                            print("#", end = "")
        print("")

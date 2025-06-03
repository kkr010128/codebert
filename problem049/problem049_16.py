while True:
    H, W = [int(x) for x in input().split(" ")]
    if H == 0 and W == 0: exit()
    for i in (range(H)):
        print("#"*W)
    print("")
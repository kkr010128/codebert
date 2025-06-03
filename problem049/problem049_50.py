while True:
    H,W = map(int, input().split())
    if H == 0 and W == 0:
        break
    elif H > 301 or W > 301:
        break
    else:
        for i in range(H):
            row = '#' * W
            print(row)
        print("\n", end ='')
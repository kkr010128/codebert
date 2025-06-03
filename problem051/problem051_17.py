while True:
    H, W = map(int, input().split())
    if H == W == 0:
        break
    
    for i in range(H):
        if i % 2 == 0:
            if W % 2 != 0:
                print("#." * (W // 2) + "#")
                continue
            print("#." * (W // 2))
        else:
            if W % 2 != 0:
                print(".#" * (W // 2) + ".")
                continue
            print(".#" * (W // 2))
    print()
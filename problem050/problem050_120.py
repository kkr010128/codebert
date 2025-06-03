while True:
        (H, W) = [int(i) for i in input().split()]
        if H == W == 0:
            break
        print ("\n".join(["".join(["#" if i == 0 or i == W - 1 or j == 0 or j == H - 1 else "." for i in range(W)]) for j in range(H)]))
        print()
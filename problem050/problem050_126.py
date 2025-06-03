while True:
    H, W = list(map(int, input().split()))
    if (H == 0) & (W == 0):
        break
        
    print(W * "#")
    for _ in range(H-2):
        print("#", end="")
        print((W-2) * ".", end="")
        print("#")
    print(W * "#")
    
    print("")
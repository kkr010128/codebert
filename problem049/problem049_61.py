while True:
    H, W = list(map(int, input().split()))
    if H == 0 & W == 0:
        break
    print(("#"*W + "\n")*H)
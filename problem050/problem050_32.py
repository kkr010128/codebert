while True:
    H, W = list(map(int, input().split()))
    if H == 0 & W == 0:
        break
    print("#"*W)
    print(("#" + "."*(W-2) + "#\n")*(H-2), end="")
    print("#"*W, end="\n\n")
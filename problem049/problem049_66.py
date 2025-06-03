while True:
    H, W = map(int, input().split())
    if (H, W) == (0, 0):
        break
    [print("#"*W+"\n") if i == H-1 else print("#"*W) for i in range(H)]
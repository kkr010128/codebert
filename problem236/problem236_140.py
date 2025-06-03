H, W, N = map(int, open(0).read().split())
if H > W:
    H, W = W, H
print((N + W - 1) // W)

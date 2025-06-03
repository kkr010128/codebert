def paint(h, w):
    print("\n".join(["#" * w] * h))

while True:
    H, W = map(int, input().split())
    if H == W == 0: break

    paint(H, W)
    print()


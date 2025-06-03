W, H, x, y, r = (int(a) for a in input().split())

if x < W and y < H and (x-r) >= 0 and (x + r) <= W and (y-r) >= 0 and (y+r) <= H:
    print("Yes")

else:
    print("No")


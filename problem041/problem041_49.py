W, H, x, y, r = [int(i) for i in input().rstrip().split(" ")]
hidari, migi = x-r, x + r
shita, ue = y-r, y+r

if (0 <= hidari) and (migi <= W) and (0 <= shita) and (ue <= H):
    print("Yes")
else:
    print("No")

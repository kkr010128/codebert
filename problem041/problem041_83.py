x = input().split()
W, H, x, y, r = int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4])

if 0 <= x-r and x+r <= W and 0 <= y-r and y+r <= H:
    print("Yes")
else:
    print("No")

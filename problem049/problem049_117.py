import sys

while 1:
    H,W = map(int, raw_input().split())

    if H == 0 and W == 0:
        break

    for i in range(H):
        for j in range(W):
            if j == W-1:
                print "#"
            else:
                sys.stdout.write("#")

        if i == H-1:
            print ""
import sys

while 1:
    H,W = map(int, raw_input().split())

    if H == 0 and W == 0:
        break

    for i in range(H):
        for j in range(W):

            if i%2 == 0:
                if j%2 == 0:
                    sys.stdout.write("#")
                else:
                    sys.stdout.write(".")

            if i%2 != 0:
                if j%2 != 0:
                    sys.stdout.write("#")
                else:
                    sys.stdout.write(".")

            if j == W-1:
                print ""

    print ""
import sys

k = 0

while k == 0:
    r = raw_input()
    H, W = r.split()
    H = int(H)
    W = int(W)
    
    if H == 0 and W == 0:
        k = 1
    else:
        for j in range(H):
            for i in range(W):
                if i == 0 or i == W-1 or j == 0 or j == H-1:
                    sys.stdout.write("#")
                else:
                    sys.stdout.write(".")
            print("")
        print("")
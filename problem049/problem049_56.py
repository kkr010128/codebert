HW = input().split()
H = int(HW[0])
W = int(HW[1])

while H != 0 or W != 0:
    for i in range(H):
        for j in range(W):
            print("#", end = "")
        print("")
    HW = input().split()
    H = int(HW[0])
    W = int(HW[1])
    print("")
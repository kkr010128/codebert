import sys
while True:
    (H, W) = [int(i) for i in sys.stdin.readline().split()]
    if H == W == 0:
        break
    line = "#." * int(W / 2 + 1)
    for i in range(H):
        if i % 2:
            print(line[1:W+1])
        else:
            print(line[:W])
    print("")
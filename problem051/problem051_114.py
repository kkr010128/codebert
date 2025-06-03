H,W = [int(x) for x in input().split()]
s = ""
while not H == W == 0:
    for i in range(H):
        for j in range(W):
            s+= "." if (i+j)%2 else "#"
        print(s)
        s = ""
    print()
    H,W = [int(x) for x in input().split()]
while True:
    H,W = map(int,input().split())
    if H == 0 and W == 0:
        break
    a = [["#" for j in range(W)] for i in range(H)]
    b = ["".join(a[i]) for i in range(H)]
    for i in range(H):
        print(b[i])
    print()
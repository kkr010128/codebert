#coding:utf-8

while True:
    H,W = input().split()
    H = int(H)
    W = int(W)
    if (H == W == 0):
        break
    else:
        for j in range(H):
            for i in range(W):
                print("#", end='')
            print()
        print()
# -*- coding: utf-8 -*-
loop = 1
while(loop):
    l = input().strip().split()
    H = int(l[0])
    W = int(l[1])
    if(H == 0 and W == 0):
        break
    else:
        for y in (range(H)):
            for x in (range(W)):
                if(x == 0 or y == 0 or x == (W-1) or y == (H-1)):
                    print("#",end="")
                else:
                    print(".",end="")
            print()
        print()
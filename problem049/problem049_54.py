# coding: utf-8
# Your code here!
while(1):
    H,W=map(int,input().split(" "))
    if H==0 and W==0:
        break
    else:
        for i in range(H):
            for j in range(W):
                print("#",end="")
            print("")
        print("")



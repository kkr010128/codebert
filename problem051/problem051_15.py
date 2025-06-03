# coding: utf-8
# Your code here!
while(1):
    H,W=map(int,input().split(" "))
    if H==0 and W==0:
        break
    for i in range(H):
        for j in range(W):
            if (i+j)%2==0:
                print("#",end="")
            else:
                print(".",end="")
        print("")
    print("")

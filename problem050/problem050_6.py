#coding:utf-8
H,W=map(int,input().split())

while not(H==0 and W==0):
    for i in range(0,H):
        for j in range(0,W):
            if i==0 or j==0 or i==H-1 or j==W-1:
                print("#",end="")
            else:
                print(".",end="")
        print("")
    print("")

    H,W=map(int,input().split())
#coding:utf-8
H,W=map(int,input().split())

while not(H==0 and W==0):
    for i in range(0,H):
        for j in range(0,W):
            print("#",end="")
        print("")
    print("")
    
    H,W=map(int,input().split())
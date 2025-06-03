n=int(input())
start=[[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for i in range(n):
    b,f,r,v=[int(i) for i in input().split()]
    start[b-1][f-1][r-1]+=v
for i in range(4):
    for j in range(3):
        for k in range(10):
            print(" ",end="")
            print(start[i][j][k],end="")
        print()
    if i<=2:
        for m in range(20):
            print("#",end="")
        print()  

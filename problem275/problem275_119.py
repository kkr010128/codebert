X,Y=map(int,input().split())
M=[0]*206
M[0],M[1],M[2]=300000,200000,100000
if X+Y==2:
    print(1000000)
else:
    print(M[X-1]+M[Y-1])
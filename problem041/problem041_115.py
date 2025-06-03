x=input().split()
W,H,x,y,r=int(x[0]),int(x[1]),int(x[2]),int(x[3]),int(x[4])
if x<r or x>W-r or y<r or y>H-r:
    print("No")
else:
    print("Yes")

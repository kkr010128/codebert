W,H,x,y,r = (int(i) for i in input().split())
if W-(x+r) >=0 and H-(y+r) >= 0:
    if x-r >= 0 and y-r >= 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
W,H,x,y,r = [int(s) for s in input().split()]
if 0 <= (x-r) <= (x+r) <= W:
    if 0 <= (y-r) <= (y+r) <= H:
        print("Yes")
    else:
        print("No")
else:
    print("No")
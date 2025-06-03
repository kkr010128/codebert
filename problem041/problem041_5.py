W,H,x,y,r = list(map(int,input().split()))

if( (W - r >= x >= 0 + r) and  (H - r >= y >= 0 + r)):
    print("Yes")
else:
    print("No")
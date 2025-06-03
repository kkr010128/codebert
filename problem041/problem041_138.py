W,H,x,y,r = input().split()
W = int(W)
H = int(H)
x = int(x)
y = int(y)
r = int(r)

if x < 0 or y < 0:
    print("No")

else:
    if W - x >= r and H - y >= r:
        print("Yes")
    else:
        print("No")
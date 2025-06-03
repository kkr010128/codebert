[W,H,x,y,r] = input().split(' ')

W = int(W)
H = int(H)
x = int(x)
y = int(y)
r = int(r)
h = False

if r<=x and x <= W - r and r <=y and y <= H - r:
    print ('Yes')
else:
    print ('No')
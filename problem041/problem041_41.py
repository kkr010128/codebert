[W,H,x,y,r] = raw_input().split(' ')
W = int(W)
H = int(H)
x = int(x)
y = int(y)
r = int(r)
h = False
if x - r >= 0:
    if x + r <= W:
        if y - r >= 0:
            if y + r <= H:
                h = True
if h:
    print 'Yes'
else:
    print 'No'
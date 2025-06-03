W,H,x,y,r = map(float,raw_input().split())
x_min = x-r
x_max=x+r
y_min=y-r
y_max=y+r

if x_min >= 0 and y_min >= 0 and x_max <= W and y_max <= H:
    print "Yes"
else:
    print "No"
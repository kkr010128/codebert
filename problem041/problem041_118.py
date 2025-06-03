w,h,x,y,r = input().split()
w = int(w)
h = int(h)
x = int(x)
y = int(y)
r = int(r)
if x - r >= 0 and y - r >= 0 and x + r <= w and y + r <= h:
    print("Yes")
else:
    print("No")

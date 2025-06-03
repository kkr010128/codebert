a = raw_input().split(" ")
W = int(a[0])
H = int(a[1])
x = int(a[2])
y = int(a[3])
r = int(a[4])
if (x - r) >= 0 and (x + r) <= W and (y - r) >= 0 and (y + r) <= H:
    print "Yes"
else:
    print "No"
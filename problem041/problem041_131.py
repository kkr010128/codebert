a = map(int, raw_input().split())
w = a[0]
h = a[1]
x = a[2]
y = a[3]
r = a[4]
if x+r <= w and x-r >= 0 and y+r <= h and y-r >= 0:
    print 'Yes'
else:
    print 'No'
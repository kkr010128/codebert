w,h,x,y,r = map(int,raw_input().split())
if w-r >= x and h-r >= y and x-r >= 0 and y-r >= 0:
    print "Yes"
else:
    print "No"
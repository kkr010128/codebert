w,h,x,y,r=map(int,raw_input().split())
if min(x,y,w-x,h-y)<r:
    print 'No'
else:
    print 'Yes'
w,h,x,y,r=map(int,raw_input().split())

f=0
if x+r>w:
    f=1
if y+r>h:
    f=1
if r>x:
    f=1
if r>y:
    f=1
if f==0:
    print "Yes"
else:
    print "No"
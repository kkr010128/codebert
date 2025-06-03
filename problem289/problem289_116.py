from math import atan, degrees
a,b,x= map(int,input().split())
yoseki = a**2*b
if x <= yoseki/2:
    # b*y*a/2==x
    y= 2*x/b/a
    # ９０からシータを引けば良い
    print(90-degrees(atan(y/b)))
else:
    # a*y*a/2==yoseki-x
    y = 2*(yoseki-x)/a**2
    print(degrees(atan(y/a)))

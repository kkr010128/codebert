t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())

d1=t1*a1+t2*a2
d2=t1*b1+t2*b2

import sys
if d1>d2:
    dif=d1-d2
    gap=(b1-a1)*t1
elif d1<d2:
    dif=d2-d1
    gap=(a1-b1)*t1
else:
    print('infinity')
    sys.exit()

if (b1-a1)*(b2-a2)>0 or (b1-a1)*(d2-d1)>0:
    print(0)
    sys.exit()
if gap%dif!=0:
    print(gap//dif*2+1)
else:
    print(gap//dif*2)
import math
import sys
x=input()
x0=x.split()
a=int(x0[0])
b=int(x0[1])
n=int(x0[2])
b0=n%b
b1=0
q1=0
if b==1:
    print(0)
    sys.exit()
for i in range(1,math.floor(n/b)+1):
    b1=b*i-1
    q1=max(q1,math.floor(a*b1/b)-a*math.floor(b1/b))
q2=math.floor(a*b0/b)-a*math.floor(b0/b)
print(max(q1,q2))
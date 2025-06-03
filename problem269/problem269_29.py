from math import ceil
t1,t2 = map(int,input().split())
a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())
a1 -= b1
a2 -= b2

if t1*a1 + t2*a2 == 0:
    print("infinity")
    exit()
if a1*a2 > 0:
    print(0)
    exit()
a1 *= t1
a2 *= t2
if (a1 > 0 and a1+a2>0) or (a1<0 and a1+a2<0):
    print(0)
    exit()

if a1 > 0:
    x = -a1/(a1+a2)
    n = ceil(x)
    if n == x:
        print(2*n)
    else:
        print(2*n-1)
if a2 > 0:
    x = a1 / (-(a1 + a2))
    n = ceil(x)
    if n == int(x):
        print(2 * n)
    else:
        print(2 * n - 1)
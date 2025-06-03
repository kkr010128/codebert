from math import ceil
t1,t2 = map(int,input().split())
a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())
a1 -= b1
a2 -= b2
a1 *= t1
a2 *= t2
if a1 + a2 == 0:
    print("infinity")
    exit()
if a1*(a1+a2) > 0:
    print(0)
    exit()

x = -a1/(a1+a2)
n = ceil(x)
if n == x:
    print(2*n)
else:
    print(2*n-1)
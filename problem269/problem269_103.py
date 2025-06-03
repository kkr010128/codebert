from math import floor
t1, t2 = map(int,input().split())
a1, a2 = map(int,input().split())
b1, b2 = map(int,input().split())

v1 = a1-b1
v2 = a2-b2

m1 = v1*t1
m2 = v2*t2

if m1>0:
    m1 *= -1
    m2 *= -1

if m1 == -m2:
    print('infinity')
elif m1+m2>0:
    ans = floor(-m1/(m2+m1)) * 2
    if m1%(m2+m1) != 0:
        ans += 1
    print(ans)
else:
    print(0)
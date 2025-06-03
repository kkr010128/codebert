import math, cmath

def koch(p1, p2, n):
    if n == 0:
        return [p1, p2]
    
    rad60 = math.pi/3
    v1 = (p2 - p1)/3
    v2 = cmath.rect(abs(v1), cmath.phase(v1)+rad60)
    q1 = p1 + v1
    q2 = q1 + v2
    q3 = q1 + v1
    if n == 1:
        return [p1,q1,q2,q3,p2]
    else:
        x1 = koch(p1,q1,n-1)[1:-1]
        x2 = koch(q1,q2,n-1)[1:-1]
        x3 = koch(q2,q3,n-1)[1:-1]
        x4 = koch(q3,p2,n-1)[1:-1]
        x = [p1]+x1+[q1]+x2+[q2]+x3+[q3]+x4+[p2]
    return x

n = int(raw_input())
p1 = complex(0,0)
p2 = complex(100,0)

for e in koch(p1,p2,n):
    print e.real,e.imag
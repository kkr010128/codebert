import math
a,b,x=map(int,input().split())
v = a * b
x = x / a
if x < v/2:
    c = x * 2 / b
    d = math.sqrt(b * b + c * c)
    print(math.degrees(math.asin(b/d)))
else:
    rest = v - x
    c = rest * 2 / a
    d = math.sqrt(a * a + c * c)
    print(math.degrees(math.acos(a/d)))
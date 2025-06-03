import math
a, b, x = map(float, input().split())

if x < a*a*b/2:
    print(math.degrees(math.atan(a*b*b/(2*x))))
else:
    print(math.degrees(math.atan(2*((a*a*b-x)/a**3))))


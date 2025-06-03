import math

def cin():
    in_ = list(map(int,input().split()))
    if len(in_) == 1:  return in_[0]
    else:  return in_

a, b, x = cin()
if a * a * b == x:  print(0)
else:
    if 2 * x <= a ** 2 * b:
        p = 2 * x / (a * b)
        print(math.degrees(math.atan(b / p)))
    else:
        S = x / a
        p = 2 * (a * b - S) / a
        print(90 - math.degrees(math.atan(a / p)))
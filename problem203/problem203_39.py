import math

A, B = map(int, input().split())

a1 = (A+1)/0.08
a2 = A/0.08
b1 = (B+1)/0.1
b2 = B/0.1


if a2 >= b1 or b2 >= a1:
    print(-1)
else:
    print(math.ceil((max(a2, b2))))
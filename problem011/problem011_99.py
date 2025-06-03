import sys
import math

(a, b) = tuple([int(s) for s in input().split()])

if a==b:
    print(a)
    sys.exit(0)

min = a if a < b else b
divisor = 1

i = 2
while i < math.sqrt(min):
    if a % i == 0 and b % i == 0:
        a = a / i
        b = b / i
        divisor = divisor * i
    else:
        i = i + 1

print(divisor)
import math
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, x = map(int, readline().split())

vol = (a ** 2) * b

if vol / 2 >= x:
    tan = 2 * x / a / (b ** 2)
    rad = math.atan(tan)
    deg = math.degrees(rad)
    ans = 90-deg
    print(ans)
else:
    tan = 2 * (a * b - x / a) / a ** 2
    rad = math.atan(tan)
    deg = math.degrees(rad)
    print(deg)

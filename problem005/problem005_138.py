def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

import fileinput
import math
for line in fileinput.input():
    a, b = map(int, line.split())
    g = gcd(a, b)
    lcm = a * b // g
    print(g, lcm)
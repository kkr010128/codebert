from math import *
PI = 3.1415926535898
while True:
    try:
        a, b = map(float, raw_input().strip().split(' '))
        print "%d %d" % (a*b, 2*(a+b))
    except EOFError:
        break
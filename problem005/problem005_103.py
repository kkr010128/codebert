import sys

while 1:
    line = sys.stdin.readline()
    if (not line):
        break
    x, y = map(int, line.split())
    if (x > y):
        gcd = x
        t = y
    else :
        gcd = y
        t = x
    while (t > 0) :
        tmp = gcd % t
        gcd = t
        t = tmp
    lcm = x * y / gcd
    print str(gcd) + " " + str(lcm)
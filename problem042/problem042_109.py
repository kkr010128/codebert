import sys

i = 1
while(True):
    x = int(sys.stdin.readline())
    if(x == 0):
        break
    print("Case %d: %d" % (i, x))
    i += 1
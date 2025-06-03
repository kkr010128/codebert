import sys
for line in sys.stdin:
    xy = sorted(map(int , line.split()))
    if xy[0] == 0 and xy[1] == 0: break
    print(*xy)
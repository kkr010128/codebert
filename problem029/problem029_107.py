# Aizu Problem ITP_1_10_A: Distance
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


x1, y1, x2, y2 = [float(_) for _ in input().split()]
print("%.8f" % math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
# Aizu Problem ITP_1_2_B: Range
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")

a, b, c = [int(_) for _ in input().split()]
print("Yes" if a < b < c else "No")
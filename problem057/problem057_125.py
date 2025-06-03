# Aizu Problem ITP_1_7_A: Grading
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


while True:
    m, f, r = [int(_) for _ in input().split()]
    score = m + f
    if m == f == r == -1:
        break
    elif m == -1 or f == -1:
        print('F')
    elif score >= 80:
        print('A')
    elif score >= 65:
        print('B')
    elif score >= 50 or (score >= 30 and r >= 50):
        print('C')
    elif score >= 30:
        print('D')
    else:
        print('F')
# Aizu Problem ITP_1_2_A: Small, Large or Equal
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")

a, b = [int(_) for _ in input().split()]
if a < b:
    print("a < b")
elif a > b:
    print("a > b")
else:
    print("a == b")
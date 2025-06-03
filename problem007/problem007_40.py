# Aizu Problem ALDS_1_10_A: Fibonacci Number
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


n = int(input())
if n < 2:
    print(1)
else:
    a, b = 1, 1
    for k in range(n - 1):
        a, b = b, a + b
    print(b)
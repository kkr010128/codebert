# Aizu Problem ITP_1_8_B: Sum of Numbers
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


while True:
    n = int(input())
    if n == 0:
        break
    print(digit_sum(n))
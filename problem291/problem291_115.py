import sys
input = sys.stdin.readline

a, b = [int(x) for x in input().split()]
if 2*b >= a:
    print(0)
else:
    print(a - 2*b)
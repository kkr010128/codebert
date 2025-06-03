from sys import stdin

A, B = [int(x) for x in stdin.readline().rstrip().split()]

if A > 2*B:
    print(A - 2*B)
else:
    print(0)
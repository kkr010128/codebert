import sys

A, B, C, D = map(int, input().split())
while A > 0 or B > 0:
    C = C - B
    if C <= 0:
        print("Yes")
        sys.exit()
    A = A - D
    if A <= 0:
        print("No")
        sys.exit()
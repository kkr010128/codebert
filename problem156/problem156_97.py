import sys
input = sys.stdin.readline

X = int(input())

A = 1
B = 0

while True:
    while A**5 - B**5 < X:
        B -= 1
    if A**5 - B**5 == X:
        print(A,B)
        exit()
    B = A
    A += 1
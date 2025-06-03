import sys

N = int(input())

p = 0

for i in range(N):
    A,B = list(map(int, input().split()))

    if A == B:
        p += 1
    else:
        p = 0

    if p == 3:
        print("Yes")
        sys.exit()

print("No")
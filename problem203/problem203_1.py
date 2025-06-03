import sys
import math
input = sys.stdin.readline

A, B = map(int, input().split())
X = A / 0.08
Y = B/0.1
for i in range(math.floor(min(X, Y)), math.ceil(max(X, Y)) + 1):
    if int(i * 0.08) == A and int(i * 0.10) == B:
        print(i)
        exit()
print(-1)

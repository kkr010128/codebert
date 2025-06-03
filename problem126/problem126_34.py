import sys
input = sys.stdin.buffer.readline


X = [int(i) for i in input().strip().split()]
print(X.index(0) + 1)

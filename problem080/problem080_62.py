import sys

readline = sys.stdin.readline
N = int(readline())
A = []
B = []
for _ in range(N):
    x, y = map(int, readline().split())
    A.append(x-y)
    B.append(x+y)
print(max(max(A) - min(A), max(B) - min(B)))
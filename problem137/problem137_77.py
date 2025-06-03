import sys

readline = sys.stdin.readline
N = int(readline())
A = []
B = []
for _ in range(N):
    a, b = map(int, readline().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
if N % 2 == 0:
    mi = A[N//2-1]+A[N//2]
    ma = B[N//2-1]+B[N//2]
else:
    mi = A[N//2]
    ma = B[N//2]
print(ma-mi+1)

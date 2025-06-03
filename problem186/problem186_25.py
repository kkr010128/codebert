import sys
read = sys.stdin.buffer.read
k, n, *A = read().split()
far = int(k) + int(A[0]) - int(A[-1])
for x, y in zip(A[1:], A):
    if far < int(x) - int(y):
        far = int(x) - int(y)
print(int(k)-far)
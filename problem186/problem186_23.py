import sys
from array import array
read = sys.stdin.buffer.read
k, n, *A = map(int, read().split())
A += [k + A[0]]
far = max(array("l", [x - y for x, y in zip(A[1:], A)]))
print(k-far)
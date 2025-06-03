import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
S, T = read().decode('utf-8').rstrip().split()

A = [None] * (N+N)
A[::2] = S
A[1::2] = T

ans = ''.join(A)
print(ans)
import sys
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
N, *A = map(int, read().split())
 
U = 10 ** 18
p = 1
for x in A:
    p *= x
    if p > U:
        p = U + 1
 
if p > U:
    print(-1)
else:
    print(p)

import sys
read = sys.stdin.buffer.read
n, k, *p = map(int, read().split())
p.sort()
print(sum(p[:k]))
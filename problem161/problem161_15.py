import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, n = map(int, readline().split())

if n >= b:
    x = b - 1
else:
    x = n

ans = (a * x) // b - a * (x // b)
print(ans)
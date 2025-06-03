import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b = map(int, readline().split())

ans = a - b * 2

if ans < 0:
    print(0)
else:
    print(ans)

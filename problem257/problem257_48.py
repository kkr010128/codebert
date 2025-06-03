import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


n = int(readline())

p = list(map(int, readline().split()))

num = 1
l = []
for i in range(n):
    if p[i] == num:
        l.append(i)
        num += 1

print('-1' if len(l) == 0 else n-len(l))

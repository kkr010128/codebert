import sys

n = int(sys.stdin.buffer.readline())
z, w = [0]*n, [0]*n
for i, a in enumerate(sys.stdin.buffer.readlines()):
    x, y = map(int, a.split())
    z[i] = x+y
    w[i] = x-y
print(max(abs(max(z)-min(z)), abs(max(w)-min(w))))

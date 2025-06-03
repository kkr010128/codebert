import sys

line_num = int(sys.stdin.readline().rstrip())
maxv = -2000000000
minv = int(sys.stdin.readline().rstrip())

for i in range(1, line_num):
    rt = int(sys.stdin.readline())
    if rt - minv > maxv:
        maxv = rt - minv
    if rt < minv:
        minv = rt

print(maxv)
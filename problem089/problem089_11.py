import sys
import io, os
#input = sys.stdin.buffer.readline
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

h, w, m = map(int, input().split())
R = [0]*h
C = [0]*w
YX = []
for i in range(m):
    y, x = map(int, input().split())
    y, x = y-1, x-1
    R[y] +=1
    C[x] +=1
    YX.append((y, x))

max_r = max(R)
max_c = max(C)
cr = 0
cc = 0
for i in range(h):
    if R[i] == max_r:
        cr += 1
for i in range(w):
    if C[i] == max_c:
        cc +=1
c = 0
for y, x in YX:
    if R[y] == max_r and C[x] == max_c:
        c += 1
if c < cr*cc:
    print(max_r+max_c)
else:
    print(max_r+max_c-1)

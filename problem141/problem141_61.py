import sys
import numpy as np
def Ii():return int(sys.stdin.buffer.readline())
def Mi():return map(int,sys.stdin.buffer.readline().split())
def Li():return list(map(int,sys.stdin.buffer.readline().split()))

n = Ii()
a = Li()
b = [0]*(n+1)
bm = [0]*(n+1)
b[0] = 1
if a[0] > 1:
  print(-1)
  exit(0)
bm[-1] = a[-1]
for i in range(1,n+1):
  bm[-1-i] = bm[-i]+a[-i-1]
  b[i] = (b[i-1]-a[i-1])*2
b = np.array(b)
bm = np.array(bm)
b = np.amin([[b],[bm]], axis=0)
if a[-1] != b[-1,-1]:
  print(-1)
  exit(0)
if np.any(b <= 0):
  print(-1)
  exit(0)
print(np.sum(b))
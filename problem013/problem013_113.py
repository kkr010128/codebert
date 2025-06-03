import sys
 
l = sys.stdin.readlines()
minv = int(l[1])
maxv = -1000000000

for r in map(int,l[2:]):
  m = r-minv
  if maxv < m: 
    maxv = m
    if m < 0: minv = r
  elif m < 0: minv = r
 
print(maxv)
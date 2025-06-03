import sys
 
n = int(input())
minv = int(input())
maxv = -1000000000
 
for r in map(int,sys.stdin.readlines()):
  m = r-minv
  if maxv < m: 
    maxv = m
    if m < 0: minv = r
  elif m < 0: minv = r
 
print(maxv)
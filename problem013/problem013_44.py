import sys

n = int(input())
minv = int(input())
v = int(input())
maxv = v-minv
if v < minv: minv = v

for r in map(int,sys.stdin.readlines()):
  m = r-minv
  if maxv < m < 0:
    maxv = m
    minv = r
  elif maxv < m:
    maxv = m
  elif m < 0:
    minv = r

print(maxv)
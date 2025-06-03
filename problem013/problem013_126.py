n = int(input())
minv = int(input())
maxv = -1000000000

for i in range(1,n):
  r = int(input())
  m = r-minv
  if maxv < m < 0:
    maxv = m
    minv = r
  elif maxv < m:
    maxv = m
  elif m < 0:
    minv = r

print(maxv)
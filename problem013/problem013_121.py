n = int(input())
minv = int(input())
maxv = -1000000000

for r in [int(input())  for i in range(1,n)]:
  maxv = max(maxv,r-minv)
  minv = min(r,minv)

print(maxv)
import sys
 
n, m = map(int, input().split())
sc = [list(map(int, input().split())) for f in range(m)]
if n == 1:
    start = 0
    end = 10
else:
    start = 10**(n-1)
    end = 10**n
for i in range(start, end):
  x = False
  for j in sc:
    if str(i)[j[0]-1] != str(j[1]):
      x = True
      break
  if x:
    continue
  print(i)
  sys.exit()
print(-1)  
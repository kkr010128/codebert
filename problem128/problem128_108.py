X, N = map(int, input().split())
if N>0:
  p = [int(i) for i in input().split()]
else:
  p = [-1]
  
p = sorted(p)
#print(p)
 
try:
  idx=p.index(X)
  flag=False
  for i in range(X+1):
    for o in [-1,+1]:
      if idx+(i*o) < 0 or idx + (i*o) >= N:
        print(X+(i*o))
        flag=True
        break
      elif X+(i*o)!=p[idx+(i*o)]:
        print(X+(i*o))
        flag=True
        break
    if flag:
      break
except:
  print(X)
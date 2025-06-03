n = int(input())
d = {}
for i in range(n):
  [b, f, r, v] = list(map(int,input().split()))
  key = f'{b} {f} {r}'
  if key in d:
    d[key] += v
  else:
    d[key] = v
    
for b in range(1,5):
  for f in range(1,4):
    for r in range(1,11):
      key = f'{b} {f} {r}'
      if key in d:
        print(" "+str(d[key]),end="")
      else:
        print(" "+str(0),end="")
      if r == 10:
        print()
      if r == 10 and f == 3 and b != 4:
        print('####################')
        

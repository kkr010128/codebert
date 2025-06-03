h,w,k = map(int,input().split())
d = []
for i in range(h):
  d.append(list(input()))

c = 0
for x in range(2**h):
  for y in range(2**w):
    e =  [['t' for _ in range(w)] for _ in range(h)]
    for i in range(h):
      if ((x >> (h-1-i)) & 1) == 1:
        for l in range(w):
          e[i][l] = 'R'
    
    for j in range(w):
      if ((y >> (w-1-j)) & 1) == 1:
        for m in range(h):
          e[m][j] = 'R'
    
    s = 0     
    for p in range(h):
      for q in range(w):
        if d[p][q] == '#' and e[p][q] != 'R':
          s += 1
    
    if s == k:
      c += 1
            
print(c)        
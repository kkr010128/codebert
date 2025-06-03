m,f,r = 0,0,0
table = []
i = 0

while m != -1 or f != -1 or r != -1:
  m,f,r = (int(x) for x in input().split())
  table.append([m,f,r])

for p in table:
  m,f,r = p[0],p[1],p[2]
  if m == -1 and f == -1 and r == -1:
    break
  if m == -1 or f == -1:
    print('F')
  elif m + f >= 80:
    print('A') 
  elif m + f >= 65:
    print('B')
  elif m + f >= 50:
    print('C')
  elif m + f >= 30:
    if r >= 50:
      print('C')
    else:
      print('D')
  else:
    print('F')

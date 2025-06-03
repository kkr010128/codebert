n,x = -1,-1
table = []
while n != 0 or x != 0:
  n,x = (int(x) for x in input().split())
  table.append([n,x])

for t in table:
  n = t[0]
  x = t[1]
  if n == 0 and x == 0:
    break
  i = 1
  s = 0
  while i < n:
    #print (i)
    if x - i > n + (n - 1):
      i += 1
      continue
    else:
      j = i + 1
      while j < n:
        #print (str(i) + "," + str(j) + "," + str(x - i - j))
        if x - i - j <= n and x - i - j > j:
          s += 1
        j += 1
      i += 1
  print (s)

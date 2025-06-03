n,m,l = (int(x) for x in input().split())

t1 = [[0 for i in range(m)] for j in range(n)]
t2 = [[0 for i in range(l)] for j in range(m)]
t3 = [[0 for i in range(l)] for j in range(n)]

i = 0
while i < n:
  t1[i] = list(int(x) for x in input().split())
  i += 1

i = 0
while i < m:
  t2[i] = list(int(x) for x in input().split())
  i += 1

# cal t3
i = 0
while i < n:
  j = 0
  while j < l:
    k,c = 0,0
    while k < m:
      #print(str(i) + " " + str(k))
      c += t1[i][k] * t2[k][j]
      k += 1
    if j != 0:
      print(' ', end='')
    print(c, end='')
    j += 1
  print ('')
  i += 1

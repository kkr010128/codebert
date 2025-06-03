r,c = (int(x) for x in input().split())

table = []
i = 0

while i < r:
  table.append(list(int(x) for x in input().split()))
  i += 1

i,j = 0,0
for i in table:
  sum = 0
  for idx,j in enumerate(i):
    if idx != 0:
      print(' ', end='')
    print(j, end='')   
    sum += j
  print(' ' + str(sum))

j,ttl = 0,0
while j < c:
  i = 0
  sum = 0
  while i < r:
    sum += table[i][j]
    i += 1
  print (sum, end=' ')
  ttl += sum
  j += 1
print(ttl)

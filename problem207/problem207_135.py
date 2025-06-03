x = []

for i in range(3):
  a =input().split()
  x.append(a)

n = int(input())
b =[input() for i in range(n)]

for i in range(3):
  for j in range(3):
    if x[i][j] in b:
      x[i][j] = '*'

for i in range(3):
    for j in range(3):
      if x[i][0] == x[i][1] == x[i][2]:
           print('Yes')
           exit()
      elif x[0][i] == x[1][i] == x[2][i]:
           print('Yes')
           exit()
      elif x[0][0] == x[1][1] == x[2][2]:
           print('Yes')
           exit()
      elif x[0][2] == x[1][1] == x[2][0]:
           print('Yes')
           exit()
   	  
print('No')
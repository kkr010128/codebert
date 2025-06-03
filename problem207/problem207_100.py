a=[list(map(int,input().split())) for i in range(3)]
n=int(input())
b=[int(input()) for i in range(n)]

d=[[0]*3 for i in range(3)]
for i in range(3):
  for j in range(3):
    if a[i][j] in b:
      d[i][j]=1
      
if d[0][0]==1 and d[0][1]==1 and d[0][2]==1:
  print('Yes')
elif d[1][0]==1 and d[1][1]==1 and d[1][2]==1:
  print('Yes')
elif d[2][0]==1 and d[2][1]==1 and d[2][2]==1:
  print('Yes')
elif d[0][0]==1 and d[1][1]==1 and d[2][2]==1:
  print('Yes')
elif d[0][0]==1 and d[1][0]==1 and d[2][0]==1:
  print('Yes')
elif d[0][1]==1 and d[1][1]==1 and d[2][1]==1:
  print('Yes')
elif d[0][2]==1 and d[1][2]==1 and d[2][2]==1:
  print('Yes')
elif d[0][2]==1 and d[1][1]==1 and d[2][0]==1:
  print('Yes')
else:
  print('No')
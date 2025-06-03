A,B,M=map(int,input().split())
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
m=[[] for i in range(M)]
for i in range(M):
  m[i]=[int(x) for x in input().split()]
  
for i in range(M):
  m[i]=a[m[i][0]-1]+b[m[i][1]-1]-m[i][2]
if(min(m)>min(a)+min(b)):
  print(min(a)+min(b))
else:
  print(min(m))
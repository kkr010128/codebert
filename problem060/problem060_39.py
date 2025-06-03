n,m,l=map(int,input().split())

#print("n:%d, m:%d, l:%d"%(n, m, l))

nmlist=[]
for i in range(n):
    nm=list(map(int,input().split()))
    nmlist.append(nm)
#print(nmlist)

mllist=[]
for j in range(m):
    ml=list(map(int,input().split()))
    mllist.append(ml)
#print(mllist)


result = []

for i in range(n):
  for j in range(l):
    sum = 0
    for k in range(m):
      sum = sum + nmlist[i][k]*mllist[k][j]
    result.append(sum)

#print(result)


for o in range(1,len(result)+1):
    if o%l==0:
        print(result[o-1])
    else:
        print(result[o-1],end=' ')
    





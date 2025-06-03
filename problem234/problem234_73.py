N=int(input())

import copy

raw=[0]*10
a=[]

for i in range(10):
  a.append(copy.deepcopy(raw))

ans=0
#print(a)

for i in range(1,N+1):
  temp=str(i)
  #print(temp)
  a[int(temp[0])][int(temp[-1])]+=1

#print(a)

for i in range(10):
  for j in range(10):
    ans+=a[i][j]*a[j][i]

print(ans)  


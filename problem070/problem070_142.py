n,m=map(int, input().split())

roads=[]

for _ in range(m):
  a,b=map(int, input().split())
  roads.append([a,b])
  
group=[i for i in range(n)]

group2=[]

while group2!=group:
  group2=list(group)
  for road in roads:
    if group[road[1]-1]>group[road[0]-1]:
      group[road[1]-1]=group[road[0]-1]
    else:
      group[road[0]-1]=group[road[1]-1]
  
counter=1
group.sort()

for i in range(n-1):
  if group[i]!=group[i+1]:
    counter+=1

print(counter-1) 
      


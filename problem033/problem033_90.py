d1=[0 for i in range(6)]
d1[:]=(int(x) for x in input().split())
t1=[0 for i in range(6)]
order=input()
for i in range(len(order)):
  if order[i]=='N':
    t1[0]=d1[1]
    t1[1]=d1[5]
    t1[2]=d1[2]
    t1[3]=d1[3]
    t1[4]=d1[0]
    t1[5]=d1[4]
  if order[i]=='S':
    t1[0]=d1[4]
    t1[1]=d1[0]
    t1[2]=d1[2]
    t1[3]=d1[3]
    t1[4]=d1[5]
    t1[5]=d1[1]
  if order[i]=='E':
    t1[0]=d1[3]
    t1[1]=d1[1]
    t1[2]=d1[0]
    t1[3]=d1[5]
    t1[4]=d1[4]
    t1[5]=d1[2]
  if order[i]=='W':
    t1[0]=d1[2]
    t1[1]=d1[1]
    t1[2]=d1[5]
    t1[3]=d1[0]
    t1[4]=d1[4]
    t1[5]=d1[3]
  
  d1=list(t1)

print(d1[0])

n=int(input())
c=0
z='No'
for i in range(n):
  x,y=map(int,input().split())
  if x==y:
    c+=1
  else:
    c=0
  if c==3:
    z='Yes'
    break
print(z)
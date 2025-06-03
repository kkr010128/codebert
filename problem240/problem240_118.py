n,m=map(int,input().split())
ac=[0]*n
wa=[0]*n
acc,wac=0,0

for i in range(m):
  p,s=input().split()
  p=int(p)
  
  if ac[p-1]==1:
    continue
    
  else:
    if s=="AC":
      ac[p-1]=1
      
    else:
      wa[p-1]+=1
      
for i in range(n):
  if ac[i]==1:
    acc+=1
    wac+=wa[i]
    
print(acc,wac)
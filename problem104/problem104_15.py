f,l,n=map(int,input().split())
ctr=0
for i in range(f,l+1):
  if i%n==0:
    ctr+=1
print(ctr)
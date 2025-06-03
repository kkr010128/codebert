n=int(input())
s=input()
ans=0
for i in range(10):
  idx1=s.find(str(i))
  for j in range(10):
    idx2=s.find(str(j),idx1+1,n)
    for k in range(10):
      idx3=s.find(str(k),idx2+1,n)
      if idx1==-1 or idx2==-1 or idx3==-1:
        continue
      else:
        ans+=1
print(ans)
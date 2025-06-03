s=input()
ans=0
tmp=0
for i in s:
  if i=='R':
    tmp+=1
  else:
    ans=max(ans,tmp)
    tmp=0
print(max(ans,tmp))

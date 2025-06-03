S=input()
T=input()

count=0
ans=0
for s in S:
  t=T[count]
  #print('t = %s, s = %s'%(t,s))
  if(t!=s):
    ans+=1
  count+=1
print(ans)
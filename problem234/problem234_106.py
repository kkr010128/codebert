n=int(input())
d={}
for i in range(1,n+1):
  f=i//(10**(len(str(i))-1))
  l=i-(i//10)*10
  if l!=0: 
    c=f*10+l
    if c in d:
      d[c]+=1
    else:
      d[c]=1
ans=0
for i in d:
  if int(str(i)[::-1]) in d:
    ans+=d[i]*d[int(str(i)[::-1])]
print(ans)
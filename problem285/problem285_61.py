s=input()
ans=0
a=[0]
for i in s:
  if i=='<':
    if a[-1]>=0:a[-1]+=1
    else:a+=[1]
  else:
    if a[-1]<0:a[-1]-=1
    else:a+=[-1]
n=len(a)
for i in range(n//2):
  i*=2
  j=i+1
  if a[i]<abs(a[j]):
    x=abs(a[j])
    y=a[i]-1
  else:
    x=abs(a[j])-1
    y=a[i]
  ans+=x*(x+1)//2+y*(y+1)//2
ans+=n%2*a[-1]*(a[-1]+1)//2
print(ans)
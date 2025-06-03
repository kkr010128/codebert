N,M=[int(i) for i in input().split()]
ans=0
for i in [N,M]:
  if i==1:
    ans += 3
  elif i==2:
    ans += 2
  elif i==3:
    ans+=1
if N==1 and M==1:
  ans+=4
print(ans*100000)
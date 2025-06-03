s=input()


s=s[::-1]
l=[0]*2019
l[0]=1
prev=0
ans=0
mul=1

for i in range(len(s)):
  now=(int(s[i])*mul)%2019
  ans+=l[(prev+now)%2019]
  l[(prev+now)%2019]+=1
  prev=(prev+now)%2019
  mul=(mul*10)%2019

print(ans)
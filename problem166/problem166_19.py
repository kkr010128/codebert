s=input()
n=len(s)
d=[0]*2019
d[0]=1
j=1
ans=0
now=0
for i in s[::-1]:
  now=(now+int(i)*j)%2019
  ans+=d[now]
  d[now]+=1
  j*=10
  j%=2019
print(ans)
n=int(input())
s=[]
t=[]
for i in range(n):
  st,tt=input().split()
  s.append(st)
  t.append(int(tt))
x=str(input())
temp=0
ans=sum(t)
for i in range(n):
  temp=temp+t[i]
  if s[i]==x:
    break
print(ans-temp)
n,a=int(input()),sorted(list(map(int,input().split())))
m=a[-1]+1
s=[0]*m
for i in a:
  s[i]+=1
for i in set(a):
  if s[i]:
    for j in range(i*2,m,i):
      s[j]=0
print(s.count(1))
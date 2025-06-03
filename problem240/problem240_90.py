n,m = map(int,input().split())
p=[0]*m
s=[0]*m
for i in range(m):
  p[i],s[i]=map(str,input().split())
cor=[0]*n
fal=[0]*n
for i in range(m):
  x=int(p[i])
  if cor[x-1]==0:
    if s[i]=='AC':
      cor[x-1]=1
    else:
      fal[x-1]+=1
ans_cor=0
ans_fal=0
for i in range(n):
  if cor[i]==1:
    ans_cor+=1
    ans_fal+=fal[i]
print(ans_cor,ans_fal) 
h,w,k=map(int,input().split())
def split(word): 
    return [char for char in word]  
      
m=[]
for i in range(h):
  m.append(input())
t=[0]*(h-1)
ans=w-1+h-1
for i in range(2**(h-1)):
  failflag=0
  s=split("{0:b}".format(i))
  s.reverse()
  for j in range(h-1-len(s)):
    s.append('0')
  s.reverse()
  a=[]
  a.append([])
  for j in range(w):
    a[0].append(int(m[0][j]))
  for j in range(1,h):
    if s[j-1]=='0':
      for l in range(w):
        a[-1][l]+=int(m[j][l])
    else:
      a.append([])
      for l in range(w):
        a[-1].append(int(m[j][l]))
  n=len(a)
  tmp=0
  p=[0]*n
  flag=0
  for j in range(w):
    for l in range(n):
      if a[l][j]>k:
        failflag=1
      if p[l]+a[l][j]>k:
        flag=1
        break
    if flag==1:
      tmp+=1
      flag=0
      for t in range(n):
        p[t]=0
    for l in range(n):
      p[l]+=a[l][j]
  if failflag==0 and n-1+tmp<ans:
    ans=n-1+tmp
print(ans)
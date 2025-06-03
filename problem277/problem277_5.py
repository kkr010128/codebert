h,w,k=map(int,input().split())
a=["x" for _ in range(h)]
c=1
if k==0:
  a=[1 for _ in range(w)]
  for i in range(h):
    print(*a)
  import sys
  sys.exit()

for i in range(h):
  s=input()
  sh=[]
  nc=0
  if s=="."*w:continue
  
  for j in range(w):
    if s[j]=="#" and nc>0:c+=1
    elif s[j]=="#": nc+=1
    sh.append(str(c))
  a[i]=sh[:]
  c+=1
  
if a[0]=="x":
  l=1
  while a[l]=="x":
    l+=1
  a[0]=a[l]
  
while "x" in a:
  for i in range(h):
    if a[i]=="x":
      l=i-1
      while a[l]=="x":
        l-=1
      a[i]=a[l]
      
for m in a:
  print(*m)
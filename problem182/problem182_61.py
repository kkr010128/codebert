n,k,c=map(int,input().split())
s=input()
if k==1:
  if s.count("o")==1:
    print(s.index("o")+1)
  exit()
l=[-c]*k
r=[n+c]*k
ll=0
for i in range(n):
  if ll==0:
    if s[i]=="o":
      l[ll]=i
      ll+=1
    continue 
  if s[i]=="x" or l[ll-1]+c>=i:continue
  l[ll]=i
  ll+=1
  if ll==k:break
rr=k-1
for i in range(n):
  if rr==k-1:
    if s[(n-1)-i]=="o":
      r[rr]=(n-1)-i
      rr-=1
    continue
  if s[(n-1)-i]=="x" or r[rr+1]-c<=(n-1)-i:continue
  r[rr]=(n-1)-i
  rr-=1
  if rr==-1:break
for i in range(k):
  if l[i]==r[i]:print(l[i]+1)
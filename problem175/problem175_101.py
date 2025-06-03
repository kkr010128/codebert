n=int(input())
s=list(input())

rn=s.count('R')
gn=s.count('G')
bn=n-rn-gn

ans=bn*gn*rn
if n>2:
  
  for x in range(n-2):
    
    y=(n-1-x)//2
    for i in range(1,y+1):
      if  (not s[x]==s[x+i]) & (not s[x]==s[x+i+i]) & (not s[x+i]==s[x+i+i]):
        ans-=1
        
  print(ans)
    
else:
  print(0)

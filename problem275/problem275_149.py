x,y=map(int,input().split())
ans=0
if x==1:
  ans=ans+300000
if y==1:
  ans=ans+300000
if x==2:
  ans=ans+200000
if y==2:
  ans=ans+200000
if x==3:
  ans=ans+100000
if y==3:
  ans=ans+100000
if x==1 and y==1:
  ans=ans+400000
print(ans)
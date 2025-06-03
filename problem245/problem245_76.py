n=int(input())
s=list(input())
flg=0
ans=0
for i in  range(n):
  if s[i]=="A":
    flg=1
  elif s[i]=="B" and flg==1:
    flg=2
  elif s[i]=="C" and flg==2:
    ans=ans+1
    flg=0 
  else:
    flg=0
print(ans)
s=str(input())
t=str(input())
ans=0
for i in range(0,len(s)-len(t)+1):
  tmp=0
  for j in range(len(t)):
    if s[i+j]==t[j]:
      tmp=tmp+1
  ans=max(ans,tmp)
print(len(t)-ans)
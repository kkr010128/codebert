s=list(input())
t=s[::-1]
ans=0
for i in range(len(s)):
  if s[i]!=t[i]:
    s[i]=t[i];s[-1-i]=t[-1-i];ans+=1
print(ans)

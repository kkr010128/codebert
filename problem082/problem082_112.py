s=input()
t=input()
ans=len(t)
for i in range(len(s)):
  if i+len(t)>len(s):break
  anss=0
  for j in range(len(t)):
    if t[j]!=s[i+j]:anss+=1
  ans=min(ans,anss)
print(ans)

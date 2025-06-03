s=input()
rs=s[::-1]
ans=0
for i in range (len(s)):
  if s[i] != rs[i]:
    ans+=1
print(ans//2)

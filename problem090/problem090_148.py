s=list(input())
count=0

if 'R' in s:
  count+=1
for i in range(len(s)-1):
  if s[i]==s[i+1] and s[i]=='R':
    count+=1
print(count)

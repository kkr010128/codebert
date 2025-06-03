s=input()
t=input()
count=0
if s==t:
  print(0)
else:
  for i in range(0,len(s)):
    if s[i]!=t[i]:
      count+=1
  print(count)
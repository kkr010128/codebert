s=list(input())
t=list(input())
x=0
for i in range(len(s)):
  if s[i]!=t[i]:
    x+=1
  else:
    pass
print(x)
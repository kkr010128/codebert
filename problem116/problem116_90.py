n=0
s=list(str(input()))
t=list(str(input()))
for i in range(len(s)):
  if s[i] != t[i]:
    n+=1
print(n)
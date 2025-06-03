s=input()
n=int((len(s)-1)/2)
c=0
for i in range(n):
  if s[i] == s[i+n+1]:
    c+=1
if c==n:
  print('Yes')
else:
  print('No')
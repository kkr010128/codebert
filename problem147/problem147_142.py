s=list(input())
t=list(input())
n=len(s)
m=len(t)

if m==n+1:
  for i in range(n):
    if s[i]==t[i]:
      continue
    if s[i]!=t[i]:
      print('No')
      exit()
  print('Yes')
  
else:
  print('No')

s=input()
n=len(s)
if s[n-1]!='s':
  s=s[0:n]+'s'
elif s[n-1]=='s':
  s=s[0:n]+'es'
print(s)

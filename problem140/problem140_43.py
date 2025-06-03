t=input()
s=''
for i in range(len(t)):
  if t[i]=='?':
    s+='D'
  else:
    s+=t[i]
print(s)
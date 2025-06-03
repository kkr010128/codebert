s=list(input())
length=len(s)
if(s[length-1]=='s'):
  s.append('es')
else:
  s.append('s')

s = ''.join(s)
print(s)

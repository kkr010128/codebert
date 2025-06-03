s=input()
t=input()
if len(s)+1==len(t) and s==t[:len(s)]:
  print('Yes')
else:print('No')
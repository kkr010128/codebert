a,b,c=map(int,input().split())
S=[a,b,c]
s=set(S)
if len(s)==2:
  print('Yes')
else:
  print('No')

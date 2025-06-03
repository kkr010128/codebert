S=input()

Slist=list(S)

flag=True

for i, c in enumerate(S):
  if i%2==0 and c!='h':
    flag=False
    break
  if i%2==1 and c!='i':
    flag=False
    break
if flag and len(S)%2==0:
  print('Yes')
else:
  print('No')
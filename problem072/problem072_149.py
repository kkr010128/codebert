c=0
for i in range(int(input())):
  d1,d2=map(int,input().split())
  if d1==d2:
    c+=1
    if c==3:
      break
  else:
    c=0

print('Yes' if c==3 else 'No')

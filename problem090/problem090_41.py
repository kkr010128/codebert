a=input()

cnt=0

for i in a:
  if i=='R':
    cnt+=1

if cnt==2 and len(a)==3:
  if a[0]=='R' and a[2]=='R':
    cnt=1

print(cnt)

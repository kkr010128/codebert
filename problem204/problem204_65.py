s=input()
q=int(input())
flag=0
t=['' for _ in range(2)]
cnt=0
for _ in range(q):
  a=list(input().split())
  if a[0]=='1':
    flag=1-flag
    cnt+=1
  else:
    if a[1]=='1':t[flag]+=a[2]
    else:t[1-flag]+=a[2]
ans=t[0][::-1]+s+t[1]
if cnt%2:ans=ans[::-1]
print(ans)
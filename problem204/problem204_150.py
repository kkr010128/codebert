s=input()
q=int(input())
f=""
b=""
r=0
for i in range(q):
  query=input().split()
  if int(query[0])==1:
    r=1-r
  else:
    if (r^(int(query[1])-1))==0:
      f+=query[2]
    else:
      b+=query[2]
ret=f[::-1]+s+b
if r:
  ret=ret[::-1]
print(ret)
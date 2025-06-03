s=list(input())
k=0
bef="x"
n=[]
ans=0
def kai(n):
  if n==0:
    return 0
  ret=0
  for i in range(1,n+1):
    ret+=i
  return ret

for i in s:
  if bef!=i:
    if bef=="x":
      st=i
      bef=i
      k+=1
      continue
    bef=i
    n.append(k)
    k=0
  k+=1
n.append(k)
n.reverse()
if st==">":
  ans+=kai(n.pop())
while len(n)!=0:
  if len(n)==1:
    ans+=kai(n.pop())
  else:
    f=n.pop()
    s=n.pop()
    if f>s:
      ans+=kai(f)+kai(s-1)
    else:
      ans+=kai(f-1)+kai(s)
    #print("{} {}".format(f,s))

print(ans)
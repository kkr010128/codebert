from collections import deque
n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a_stack=deque([])
now=0
mn=0
j=0
for i in a:
  mn+=i
  if mn>k:
    mn-=i
    break
  else:
    now+=1
    a_stack.append(i)
for i in b:
  mn+=i
  if mn>k:
    mn-=i
    break
  else:
    now+=1
    j+=1
    if j==m:
      print(now)
      exit()
ans=now
while a_stack:
  if j>=m:
    break
  else:
    q=a_stack.pop()
    mn-=q
    now-=1
    while k-mn>0:
      mn+=b[j]
      now+=1
      if k-mn<0:
        now-=1
        mn-=b[j]
        break
      j+=1
      if j==m:
        break
    ans=max(now,ans)
print(ans)
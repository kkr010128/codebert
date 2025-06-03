n,k=map(int,input().split())
ans=[]
if n%2==1:
  a=1
  b=n
  for _ in range(k):
    ans.append([a,b])
    a+=1
    b-=1
else:
  a=1
  b=n
  s=set()
  for _ in range(k):
    s.add(abs(a-b))
    s.add(abs(n+a-b)%n)
    ans.append([a,b])
    a+=1
    b-=1
    if abs(a-b) in s or abs(n+a-b)%n in s or abs(a-b)==abs(n+a-b):
      b-=1
for i in range(k):
  print(*ans[i])
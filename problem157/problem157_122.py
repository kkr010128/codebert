n=int(input())
a=list(map(int,input().split()))
thing={}
ans=0
for i in range(n):
  if i-a[i] in thing:
    ans+=thing[i-a[i]]
  if i+a[i] in thing:
    thing[i+a[i]]+=1
  else:
    thing[i+a[i]]=1
print(ans)
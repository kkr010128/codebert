n,m=map(int,input().split())
h=list(map(int,input().split()))
data=[[] for _ in range(n)]
for i in range(m):
  a,b=map(int,input().split())
  data[a-1].append(b-1)
  data[b-1].append(a-1)
ans=0
for i in range(n):
  for j in data[i]:
    if h[i]<=h[j]:
      break
  else:
    ans+=1
print(ans)
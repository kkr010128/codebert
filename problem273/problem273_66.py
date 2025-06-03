n,k=map(int,input().split())
a=list(map(int,input().split()))
current=[0]
dic={}
dic[0]=1
ans=0
for i in range(n):
  current.append((current[-1]+a[i]-1)%k)
  if i>=k-1:
    dic[current[-k-1]]-=1
  if current[-1] in dic:
    ans+=dic[current[-1]]
    dic[current[-1]]+=1
  else:
    dic[current[-1]]=1
print(ans)
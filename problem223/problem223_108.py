n,k=map(int,input().split())
li=list(map(int,input().split()))
kai=[0]
for i in range(1,1001):
  kai.append(kai[i-1]+i)
ka=[0]+[kai[i]/i for i in range(1,len(kai))]
lis=[ka[i] for i in li]

ans=sum(lis[:k])
mx=ans
for i in range(len(li)-k):
  ans-=lis[i]
  ans+=lis[i+k]
  mx=max(ans,mx)
print(mx)

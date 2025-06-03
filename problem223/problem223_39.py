n,k=map(int,input().split())
a=list(map(int,input().split()))

rui=[0]
for i in a:
  rui.append(rui[-1]+i)
hantei=0
for i in range(0,len(rui)-k):
  if hantei<=rui[i+k]-rui[i]:
    hantei=rui[i+k]-rui[i]
    l=i
    r=i+k
ans=0
for i in range(l,r):
  ans+=(a[i]+1)/2
  
print(ans)
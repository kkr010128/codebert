n,k=map(int,input().split())
h=list(map(int,input().split()))
res=0
for i in range(n):
  res += (h[i] >= k)
print(res)
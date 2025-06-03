n=int(input())
minv=int(input())
maxv=-float('inf')
for _ in range(n-1):
  tmp=int(input())
  maxv=max(maxv,tmp-minv)
  minv=min(minv,tmp)
print(maxv)

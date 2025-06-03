n=int(input())
L=sorted(list(map(int,input().split())))
ans=0
for i in range(n):
  for j in range(i+1,n):
    l=j;r=n
    while abs(l-r)>1:
      mid=(r+l)//2
      if L[i]<L[j]+L[mid] and L[j]<L[i]+L[mid] and L[mid]<L[i]+L[j]:
        l=mid
      else: r=mid
    ans+=l-j
print(ans)
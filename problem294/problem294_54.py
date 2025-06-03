n=int(input())
l=sorted(list(map(int,input().split())))
ans=0
for i in range(n):
  for j in range(i+1,n):
    left=j+1
    right=n
    while left<right:
      mid=(left+right)//2
      if l[mid]>=l[i]+l[j]:
        right=mid
      else:
        left=mid+1
    ans+=right-j-1
print(ans)
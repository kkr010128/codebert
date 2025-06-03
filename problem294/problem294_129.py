n=int(input())
l=list(map(int,input().split()))

l.sort(reverse=True)
ans=0

for i in range(0,n-2):
  for j in range(i+1,n-1):
    left = j
    right = n
    while right-left>1:
      mid = (left + right)//2
      
      if l[i]+l[j]>l[mid] and l[i]+l[mid]>l[j] and l[mid]+l[j]>l[i]:
        left = mid
      else:
        right = mid
    #print(i,j,left)
    ans+=(left-j)
      
print(ans)
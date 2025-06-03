k=int(input())
a=list(map(int,input().split()))
ans=[0 for x in range (2*(10**5))]
for i in range(k-1):
  ans[(a[i]-1)]+=1
for i in range(k):
  print(ans[i])
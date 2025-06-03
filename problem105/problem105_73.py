N = int(input())
a=list(map(int,input().split()))
count=0
for i in range(1,N+1):
  if i%2==1:
    if a[i-1]%2==1:
      count +=1
print(count)
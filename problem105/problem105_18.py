N=int(input())
l=list(map(int,input().split()))
count=0
for k in range(1,N+1):
  if k%2==1 and l[k-1]%2==1:
    count+=1
print(count)
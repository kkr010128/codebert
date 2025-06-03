n=int(input())
array=list(map(int,input().split()))
ans=0
for m in range(n):
  if m%2==0 and array[m]%2==1:
    ans=ans+1
print(ans)
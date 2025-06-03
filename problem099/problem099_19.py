N,K=map(int,input().split())
A=list(map(int,input().split()))
a=0
b=10**9+1
while a+1<b:
  mid=(a+b)//2
  ans=0
  for i in A:
    ans+=(i-1)//mid
  if K<ans:
    a=mid
  else:
    b=mid
print(b)
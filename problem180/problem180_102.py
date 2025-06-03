n,k=map(int,input().split())
while n>k:
  n=n%k
if n>k//2:
  n=abs(n-k)
print(n)
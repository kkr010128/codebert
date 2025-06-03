n,k=map(int,input().split())
s=list(map(int,input().split()))
z=0
for i in range(n):
  if s[i]>=k:
    z+=1
print(z)
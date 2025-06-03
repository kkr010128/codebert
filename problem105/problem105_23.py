N=int(input())
a=list(map(int,input().split()))
z=0
for i in range(0,N,2):
  if int(a[i])%2==1:
    z+=1
print(z)



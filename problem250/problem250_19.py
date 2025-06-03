X=int(input())
n=100004
L=[True]*n
L[0]=False
L[1]=False
for i in range(2,int(n**0.5)+1):
  if L[i]:
    for j in range(i*2,n):
      if j%i==0:
        L[j]=False
for i in range(X,n):
  if L[i]==True:
    print(i)
    exit()
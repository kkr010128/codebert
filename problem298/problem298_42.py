N,K=input().split()
N=int(N)
K=int(K)
ls=[int(s) for s in input().split()]
count=0
for i in range(N):
  if ls[i]>=K:
    count=count+1
print(count)
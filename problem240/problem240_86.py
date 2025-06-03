N,M=map(int, input().split())
a=[0]*(N+1)
w=[0]*(N+1)

for _ in range(M):
  p,s=input().split()
  p=int(p)
  if s=='AC':
    a[p]=1
  else:
    if a[p]==0:
      w[p]+=1

a2=0
w2=0
for n in range(N+1):
  if a[n]==1:
    a2+=a[n]
    w2+=w[n]
      
print(a2, w2)

N,K=map(int,input().split())
p=list(map(int,input().split()))
q=[]
q.append(0)
for i in range(len(p)):
  q.append(q[-1]+p[i])
maxi=q[K]-q[0]
for i in range(1,N-K+1):
  sub=q[K+i]-q[i]
  if sub>=maxi:
    maxi=sub
print((maxi+K)/2)
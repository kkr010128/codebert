N,K=map(int,input().split())
P=list(map(lambda x: (int(x)+1)/2,input().split()))
s=tmp=sum(P[:K])
for i in range(K,N):
  tmp=tmp-P[i-K]+P[i]
  s=max(s,tmp)
print(s)
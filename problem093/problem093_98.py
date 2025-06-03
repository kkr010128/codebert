N,K=map(int,input().split())
P=list(map(int,input().split()))
P=list(map(lambda x:x-1,P)) 
C=list(map(int,input().split()))
ans=-float("inf")
for i in range(N):
   st=i
   tmp=0
   for j in range(K):
      st=P[st]
      tmp+=C[st]
      ans=max(ans,tmp)
      if i==st:
         break
   s,v=divmod(K,j+1)
   if s>1 and v==0:
      s-=1
      v=j+1
   tmp*=s
   ans=max(ans,tmp)
   for j in range(v):
      st=P[st]
      tmp+=C[st]
      ans=max(ans,tmp)
print(ans)
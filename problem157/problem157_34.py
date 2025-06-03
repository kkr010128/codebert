N=int(input())
 
A=list(map(int,input().split()))
#B=[]
#C=[]
D=[0]*1000000
E=[0]*1000000
 
ans=0
 
for i in range(N):
  if A[i]<500000:
  #B.append(A[i]+i+1)
  #C.append(-A[i]+i+1)
  #if -A[i]+i>=0:
  	D[A[i]+i]+=1
  	E[-A[i]+i]+=1
   #print(E[-A[i]+i],-A[i]+i)

for i in range(1000000):
  #ans+=C.count(i)
  ans+=D[i]*E[i]
 
print(ans)
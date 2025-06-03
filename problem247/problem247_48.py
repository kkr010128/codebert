import fractions
N,M = map(int,input().split())
A = list(map(int,input().split()))
t=1
while A:
 b=0
 for i in range(N):
  A[i]=int(A[i]/2)
  if A[i]%2==1:
   b+=1
 if b==N:
  break
 elif 0<b<N:
  t=0
  break
 else:
  t+=1
if t==0:
 print(0)
else:
 ans = A[0]
 for i in range(1, N):
  ans = ans * A[i] // fractions.gcd(ans, A[i])
 ans=min(ans,(M+1))
 c=int(M/(2**(t-1))/ans)
 d=int(M/(2**(t))/ans)
 print(c-d)
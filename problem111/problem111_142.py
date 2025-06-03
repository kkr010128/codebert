N=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
ans=A[0]
if N%2==1:
  n=int((N-1)/2)
  ans+=A[n]
  for i in range(1,n):
    ans+=2*A[i]
elif N==2:
  ans+=0
elif N%2==0 and N>2:
  n=int((N-2)/2)
  for i in range(1,n+1):
    ans+=2*A[i]
print(ans)